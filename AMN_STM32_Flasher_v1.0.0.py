# ----------------------------------------------------------------------
# AMN STM32 Flasher v1.0.0
# The First Drag-and-Drop Firmware Flasher
# ----------------------------------------------------------------------
# Copyright 2025 Aneesh Murali Nariyampully
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------
# Description:
#   AMN STM32 Flasher is the first drag-and-drop firmware flashing tool
#   for STM32 microcontrollers. It provides a clean, modern, and
#   user-friendly GUI to flash .bin firmware files directly using
#   ST-LINK_CLI.exe from STMicroelectronics.
#
# Legal Notice:
#   This software does NOT include, distribute, or modify any
#   STMicroelectronics property. Users must have the official
#   ST-LINK Utility and ST-LINK USB drivers installed separately.
# ----------------------------------------------------------------------
# Module Main: AMN_STM32_Flasher_v1.0.0.py
# Purpose:
#   Main GUI and core logic — drag-and-drop flashing, progress control,
#   ST-LINK CLI handling, Drop Flash automation, and RDP protection.


from amn_instance import ensure_single_instance, release_single_instance
import os
import customtkinter as ctk
from amn_drop import AMNDropMixin
from amn_dragout import enable_amn_drag_out
from amn_drag_simulator import AMNDragSimulator
import subprocess
import time
from pathfinder import find_path
import json
from formatter import format_firmware_name
from theme import theme
from customtkinter.windows.widgets.theme import theme_manager
import shutil
from tkinter import filedialog, messagebox
import threading
from pathlib import Path
import queue
update_queue = queue.Queue()
#---------------Global Constants and Defaults--------------------------

# Define Documents and App folder
DOCUMENTS_FOLDER = os.path.join(os.path.expanduser("~"), "Documents")
APP_FOLDER = os.path.join(DOCUMENTS_FOLDER, "AMNSTM32Flasher")
os.makedirs(APP_FOLDER, exist_ok=True)

# Key files inside Documents/AMNSTM32Flasher
CACHE_FILE = os.path.join(APP_FOLDER, "cache.amn")
SETTINGS_FILE = os.path.join(APP_FOLDER, "settings.json")

# Global runtime variables
STLINK_CLI_PATH = None
FIRMWARE_FILE = None
FLASH_START_ADDR = "0x08000000"
DROP_FLASH = "ENABLED"
DROP_FLASH_ENABLED_COLOR = "#ff9600"
DROP_FLASH_DISABLED_COLOR = "#2b2d30"
DROP_FLASH_HOVER_COLOR = "#03dac6"

CREATE_NO_WINDOW = 0x08000000
FLASHING = False
# Default settings
DEFAULT_SETTINGS = {
    "FLASH_START_ADDR": FLASH_START_ADDR,
    "DROP_FLASH":DROP_FLASH
}

# Ensure cache file exists at startup (GUI-safe, no print)
try:
    if not os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            f.write("")  # create empty cache file
except Exception:
    # Do nothing visible — GUI will handle errors later if needed
    pass

# --- Theme Initialization ---
theme_Dark_Purple_Green_By_AMN = theme
theme_manager.ThemeManager.theme = theme_Dark_Purple_Green_By_AMN
theme_manager.ThemeManager._current_theme_name = "Dark_Purple_Green_By_AMN"
ctk.set_default_color_theme = lambda *a, **k: None
ctk.ThemeManager.load_theme = lambda *a, **k: None
try:
    theme_manager.ThemeManager.load_theme("Dark_Purple_Green_By_AMN")
except Exception:
    pass
ctk.set_appearance_mode("Dark")




class FlasherApp(ctk.CTk,AMNDropMixin):
    def __init__(self):
        super().__init__()
        self.scanning = False
        self.title("AMN STM32 Flasher")
        self.geometry("550x190")
        self.resizable(False, False)
        self.iconbitmap("assets/amnflasher.ico")
        self.bind("<Map>", lambda e: self.after(50, self._restore_geometry))

        # Status label
        self.status_label = ctk.CTkLabel(self, text="", font=("Helvetica", 14))
        self.status_label.pack(pady=(30, 10))


        # Progress bar
        self.progress = ctk.CTkProgressBar(self, width=500)
        self.progress.pack(pady=10)
        self.progress.set(0)

        # Frame for checkbox + button
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20)

        # ⚡ Indicate Drop Flash ENABLED
        self.drop_flash_label = ctk.CTkLabel(
            master=button_frame,
            text="⚡",
            font=("Helvetica", 22),
            text_color=DROP_FLASH_DISABLED_COLOR
        )
        self.drop_flash_label.pack(side="left", padx=(0, 8), pady=5)

        # Check Box Protection
        self.rdp_var = ctk.BooleanVar(value=False)
        self.rdp_checkbox = ctk.CTkCheckBox(
            master=button_frame,
            text="Enable Firmware Protection",
            border_width=2,
            variable=self.rdp_var,
            font=("Helvetica", 14),
            state="normal"
        )
        self.rdp_checkbox.pack(side="left", padx=(0, 60), pady=5)

        # Install/Add Firmware button
        self.flash_btn = ctk.CTkButton(
            button_frame,
            text="Install",
            corner_radius=5,
            height=30,
            width=175,
            font=("Helvetica", 14, "bold"),
            state="disabled"  # Initially disabled until ST-LINK is found
        )
        self.flash_btn.pack(side="right")

        # --- Safe close ---
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Start searching for ST-LINK_CLI.exe in background
        threading.Thread(target=self.locate_stlink, daemon=True).start()

        #drop flash label hover effect
        def on_enter_flash_label(event):
            self.drop_flash_label.configure(text_color=DROP_FLASH_HOVER_COLOR)

        def on_leave_flash_label(event):
            if DROP_FLASH == "ENABLED":
                self.drop_flash_label.configure(text_color=DROP_FLASH_ENABLED_COLOR)
            else:
                self.drop_flash_label.configure(text_color=DROP_FLASH_DISABLED_COLOR)


        self.drop_flash_label.bind("<Enter>",on_enter_flash_label)
        self.drop_flash_label.bind("<Leave>",on_leave_flash_label)

        # Bind  keys to handle Keyboard Shortcut events
        self.bind("<Key-q>", self.handle_drop_flash_key)
        self.bind("<Key-Q>", self.handle_drop_flash_key)  # also uppercase
        self.bind("<Delete>", self.handle_delete_key)
        self.bind("<KP_Delete>", self.handle_delete_key)
        self.bind("<D>", self.handle_delete_key)
        self.bind("<d>", self.handle_delete_key)
        self.bind("<Key-I>", self.handle_flash_key)
        self.bind("<Key-i>", self.handle_flash_key)
        self.bind("<Key-a>", self.handle_add_key)
        self.bind("<Key-A>", self.handle_add_key)
        self.bind("<Return>", self.handle_return_key)  # <Return> is Enter
        self.bind("<KP_Enter>", self.handle_return_key)  # Numpad Enter
        self.bind("<p>", self.handle_rdp_checkbox_key)
        self.bind("<P>", self.handle_rdp_checkbox_key)
        self.bind("<e>", self.handle_rdp_checkbox_key)
        self.bind("<E>", self.handle_rdp_checkbox_key)
        self.drop_flash_label.bind("<Button-1>",self.drop_flash_label_clicked)
        self.enable_drop(self.on_drop)
        self.drag_sim = AMNDragSimulator(
            app=self,
            widget=self.status_label,
            get_text_func=lambda: (f"⚡  Installing {format_firmware_name(FIRMWARE_FILE)}...\nplease wait..." if FLASHING else f"📄 {format_firmware_name(FIRMWARE_FILE)}" if FIRMWARE_FILE else ""),
            condition_func=lambda: (not FLASHING or FLASHING) and (FIRMWARE_FILE is not None)
        )
        enable_amn_drag_out(self.status_label, self.on_drag_out)
        self.after(50,self.check_update_queue)

    def on_drop(self, files):
        file_path  = files[0]
        if not file_path:
            return
        dest_path = Path(APP_FOLDER) / Path(file_path).name
        if not file_path.lower().endswith(".bin"):
            messagebox.showwarning(
                "Unsupported File Type",
                "This file type isn’t supported.\nPlease drop a valid .bin firmware file."
            )
            return

                    # Allow drop only if button text is 'Add Firmware'
                    # current_text = self.flash_btn.cget("text")
                    # current_text == "Add Firmware" :
        if not FLASHING:
            try:
                #Delete existing .bin files in the directory before copying
                for old_bin in Path(APP_FOLDER).glob("*.bin"):
                    try:
                        old_bin.unlink()
                    except Exception as e:
                        messagebox.showwarning("Warning",  f"Could not delete firmware file '{old_bin.name}'.\n\nDetails: {e}")
                shutil.copy(file_path, dest_path)
            except Exception as e:
                messagebox.showerror(
                    "Copy Issue",
                    f"The firmware could not be copied to your workspace. Please try again.\n{e}"
                )
                return
            update_queue.put(dest_path)

    def check_update_queue(self):
        try:
            while True:
                dest=update_queue.get_nowait()
                self.drop_ui_update(dest)
        except queue.Empty:
            pass
        self.after(50,self.check_update_queue)
    def drop_ui_update(self,dest_path):
        global FIRMWARE_FILE
        FIRMWARE_FILE = dest_path.name
        self.update_status(f"🚀  Ready to install {format_firmware_name(FIRMWARE_FILE)}")
        self.flash_btn.configure(text="Install", state="normal", command=self.start_flash)
        self.progress.set(0)
        if DROP_FLASH == "ENABLED":
            self.start_flash()

    def on_drag_out(self):
        if not FLASHING:
            self.progress.set(0)
            global FIRMWARE_FILE

            if not FIRMWARE_FILE:
                self.update_status("💡  You haven’t added a firmware file yet.")
                return

            try:
                firmware_path = Path(APP_FOLDER) / FIRMWARE_FILE
                if firmware_path.exists():
                    firmware_path.unlink()

                FIRMWARE_FILE = None
                self.update_status("🧽  Firmware cleared from workspace.")
                self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
            except Exception as e:
                messagebox.showerror(
                    "Unexpected Issue!",
                    f"Something went wrong while removing the firmware. Please try again.\n{e}"
                )


    def on_close(self):
        self.destroy()

    def _restore_geometry(self):
        # Fix tiny window issue when restored from minimized state."""
        try:
            self.geometry("550x190")  # reapply your default size
            self.lift()
            self.focus_force()
        except Exception:
            pass

    # ---------------- Settings ----------------
    def load_settings(self): # Load settings.json from Documents/AMNSTM32Flasher, create it if missing.
        global FLASH_START_ADDR,DROP_FLASH

        try:
            # Create default file if it doesn't exist
            if not os.path.exists(SETTINGS_FILE):
                with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(DEFAULT_SETTINGS, f, indent=4)

            # Load file
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                settings = json.load(f)

            # Apply or fallback
            FLASH_START_ADDR = settings.get("FLASH_START_ADDR", DEFAULT_SETTINGS["FLASH_START_ADDR"])
            DROP_FLASH = settings.get("DROP_FLASH", DEFAULT_SETTINGS["DROP_FLASH"])
            self.update_drop_flash_label()

        except Exception as e:
            messagebox.showerror(
                "Settings Issue",
                f"Settings could not be loaded.\n{e}"
            )

            self.destroy()

    # ---------------- Firmware Browse ----------------
    def browse_firmware(self): # Select firmware (.bin), copy it to Documents/AMNSTM32Flasher, and update UI.
        self.progress.set(0)
        file_path = filedialog.askopenfilename(
            title="Select Firmware (.bin)",
            filetypes=[("Binary files", "*.bin")]
        )
        if not file_path:
            return

        dest_path = Path(APP_FOLDER) / Path(file_path).name
        try:
            shutil.copy(file_path, dest_path)
        except Exception as e:
            messagebox.showerror(
                "Copy Issue",
                f"The firmware could not be copied to your workspace.\nPlease try again.\n{e}"
            )
            return

        global FIRMWARE_FILE
        FIRMWARE_FILE = dest_path.name
        self.update_status(f"🚀  Ready to install {format_firmware_name(FIRMWARE_FILE)}")
        self.flash_btn.configure(text="Install", state="normal", command=self.start_flash)

    def handle_delete_key(self, event): #Delete firmware file from Documents/AMNSTM32Flasher (no confirmation).
        if not FLASHING:
            self.progress.set(0)
            global FIRMWARE_FILE

            if not FIRMWARE_FILE:
                self.update_status("💡  Add a firmware file first.")
                return

            try:
                firmware_path = Path(APP_FOLDER) / FIRMWARE_FILE
                if firmware_path.exists():
                    firmware_path.unlink()

                FIRMWARE_FILE = None
                self.update_status("🧽  Firmware cleared from workspace.")
                self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
            except Exception as e:
                messagebox.showerror(
                    "Delete Issue",
                    f"The firmware could not be removed. Please try again.\n{e}"
                )


    def update_drop_flash_label(self):
        if DROP_FLASH == "ENABLED":
            self.drop_flash_label.configure(text_color=DROP_FLASH_ENABLED_COLOR)
            return
        self.drop_flash_label.configure(text_color=DROP_FLASH_DISABLED_COLOR)

    def toggle_drop_flash(self):
        global DROP_FLASH
        # Toggle Drop Flash
        if DROP_FLASH == "ENABLED":
            DROP_FLASH = "DISABLED"
            self.drop_flash_label.configure(text_color=DROP_FLASH_DISABLED_COLOR)
        else:
            DROP_FLASH = "ENABLED"
            self.drop_flash_label.configure(text_color=DROP_FLASH_ENABLED_COLOR)


    def update_dropflash_settings(self):
        try:
            # Update JSON file
            with open(SETTINGS_FILE, "r") as s:
                settings = json.load(s)
                settings["DROP_FLASH"] = DROP_FLASH
            with open(SETTINGS_FILE, "w") as s:
                json.dump(settings, s, indent=4)
        except Exception :
            messagebox.showerror(
                "Settings Error",
                f"The settings file couldn’t be loaded."
            )


    # If Q pressed run this
    def handle_drop_flash_key(self,event):
        self.toggle_drop_flash()
        self.update_dropflash_settings()

    # If mouse left-clicked on flash icon run this
    def drop_flash_label_clicked(self,event):
        self.toggle_drop_flash()
        self.update_dropflash_settings()





    # ---------------- Path Finder ----------------
    def locate_stlink(self): # Locate ST-LINK_CLI.exe, load settings, and check for firmware.
        global STLINK_CLI_PATH, FIRMWARE_FILE
        self.scanning = True
        self.animate_scanning()
        start_dirs = [r"C:\Program Files (x86)\STMicroelectronics\STM32 ST-LINK Utility\ST-LINK Utility"]

        # --- Check cache ---
        cached_path = None
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as cache_amn:
                    cached_path = cache_amn.read().strip()
                if cached_path and os.path.exists(cached_path):
                    cached_dir = os.path.dirname(cached_path)
                    if cached_dir not in start_dirs:
                        start_dirs.insert(0, cached_dir)
            except Exception:
                cached_path = None

        # --- Locate executable ---
        STLINK_CLI_PATH = find_path("ST-LINK_CLI.exe", start_dirs=start_dirs)
        if STLINK_CLI_PATH is None:
            STLINK_CLI_PATH = find_path("ST-LINK_CLI.exe")
        self.scanning = False

        if STLINK_CLI_PATH:
            # Update cache if changed
            if cached_path != STLINK_CLI_PATH:
                try:
                    with open(CACHE_FILE, "w", encoding="utf-8") as f:
                        f.write(STLINK_CLI_PATH)
                except Exception as e:
                    self.update_status(f"⚠️  The cache couldn’t be updated. {e}")


            # Load settings
            self.load_settings()

            # Find firmware
            firmware_files = list(Path(APP_FOLDER).glob("*.bin"))
            FIRMWARE_FILE = firmware_files[0].name if firmware_files else None

            # Update UI
            if not FIRMWARE_FILE:
                self.update_status("💡 No firmware yet. Drag a .bin file to begin.")
                self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
            else:
                self.update_status(f"🚀  Ready to install {format_firmware_name(FIRMWARE_FILE)}")
                self.flash_btn.configure(text="Install", state="normal", command=self.start_flash)
        else:
            self.update_status("🔍 ⚠️ ST-LINK Utility not found. Please install it first.")
            self.flash_btn.configure(state="disabled")

    # ---------------- GUI Updates ----------------
    def animate_scanning(self):    # Ultra-smooth 60 FPS scanning animation with auto-reset progress bar.
        dots = ["    ", ".   ", "..  ", "... "]
        frame = 0
        progress = 0.0
        direction = 1
        fps_interval = int(1000 / 60)  # 60 FPS (~16 ms per frame)

        def loop():
            nonlocal frame, progress, direction

            # Stop cleanly when scanning flag is off
            if not getattr(self, "scanning", False):
                # Graceful progress reset to 0
                if progress > 0:
                    progress = max(0, progress - 0.02)
                    self.progress.set(progress)
                    self.after(fps_interval, loop)
                else:
                    self.progress.set(0)
                return

            # Animate scanning label every ~0.5 s
            if frame % 30 == 0:  # 60 fps * 0.5s = 30 frames
                dot = dots[(frame // 30) % len(dots)]
                self.update_status(f"🔍  Searching for ST-LINK Utility{dot}")

            # Smooth ping-pong motion for the progress bar
            progress += direction * 0.01
            if progress >= 1.0:
                progress = 1.0
                direction = -1
            elif progress <= 0.0:
                progress = 0.0
                direction = 1
            self.progress.set(progress)

            frame += 1
            self.after(fps_interval, loop)

        loop()

    def update_status(self, text):
        self.after(0, lambda: self.status_label.configure(text=text))


    def update_progress(self, value):
        self.after(0, lambda: self.progress.set(value / 100))


    # ---------------- Flashing ----------------
    def start_flash(self):
        self.flash_btn.configure(state="disabled")
        threading.Thread(target=self.flash_firmware, daemon=True).start()

    def handle_flash_key(self,event):
        if not FLASHING:
            if self.flash_btn.cget("text").lower() == "install":
                self.start_flash()

    def handle_return_key(self,event):
        if not FLASHING:
            if self.flash_btn.cget("text").lower() == "install":
                self.start_flash()
            elif self.flash_btn.cget("text").lower() == "add firmware":
                self.browse_firmware()

    def handle_add_key(self,event):
        if not FLASHING:
            if self.flash_btn.cget("text").lower() == "add firmware":
                self.browse_firmware()

    def handle_rdp_checkbox_key(self, event):
        if not FLASHING:
            self.rdp_checkbox.toggle()




    def enable_rdp1(self):
        global FLASHING
        self.update_status("🛡️ Finalizing protection settings...")
        try:
            result = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-OB", "RDP=1", "-Rst"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=CREATE_NO_WINDOW
            )
            if result.returncode != 0:
                raise RuntimeError(f"Couldn’t enable protection!\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
            self.update_status("🔒 Protection enabled successfully.")
        except Exception as e:
            FLASHING = False
            self.update_status("⚠️ Couldn’t enable protection.")
            messagebox.showerror("Protection Configuration", f"The firmware was installed successfully, but security could not be enabled:\n{str(e)}")

    def flash_firmware(self):
        global FLASHING
        FLASHING = True
        # """Flash and verify firmware from Documents/AMNSTM32Flasher using ST-LINK_CLI."""
        self.update_status("⚙️ Preparing...")
        self.animate_progress(0, 10)

        # --- ST-LINK CLI check ---
        if not STLINK_CLI_PATH or not Path(STLINK_CLI_PATH).exists():
            FLASHING = False
            messagebox.showerror("ST-LINK Utility Missing", f"The ST-LINK Utility could not be found. Make sure it’s installed:\n{STLINK_CLI_PATH}")
            self.flash_btn.configure(state="normal")
            self.update_status("🛠️ Fix the issue and retry.")
            self.update_progress(0)
            return

        # --- Firmware path check ---
        firmware_path = Path(APP_FOLDER) / FIRMWARE_FILE
        if not firmware_path.exists():
            FLASHING = False
            messagebox.showerror("Error", f"Firmware file not found:\n{firmware_path}")
            self.flash_btn.configure(state="normal")
            self.update_status("⚠️  Firmware not found. Add it again to continue.")
            self.update_progress(0)
            self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
            return

        try:
            # --- Disable RDP ---
            self.update_status("🔧 Disabling protection...")
            result_erase = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-OB", "RDP=0", "-Rst"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=CREATE_NO_WINDOW
            )
            if result_erase.returncode != 0:
                raise RuntimeError(f"Couldn’t enable protection:\n{result_erase.stdout}\n{result_erase.stderr}")
            self.animate_progress(10, 35)

            # --- Full chip erase ---
            self.update_status("🧽  Clearing device memory...")
            result_erase = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-ME", "-Rst"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=CREATE_NO_WINDOW
            )
            if result_erase.returncode != 0:
                raise RuntimeError(f"Chip erase failed:\n{result_erase.stdout}\n{result_erase.stderr}")
            self.animate_progress(35, 50)

            # --- Flash + Verify firmware ---
            self.update_status(f"⚡ Installing {format_firmware_name(FIRMWARE_FILE)}  ⏳")
            result_flash = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-P", str(firmware_path), FLASH_START_ADDR, "-V", "-Rst"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=CREATE_NO_WINDOW
            )
            if result_flash.returncode != 0:
                raise RuntimeError(f"Couldn’t complete installation:\n{result_flash.stdout}\n{result_flash.stderr}")
            self.animate_progress(50, 95)

            # --- Enable RDP (if selected) ---
            if self.rdp_var.get():
                self.enable_rdp1()

            self.animate_progress(95, 100)
            self.update_status("✅  Installation complete.")

        except Exception as e:
            FLASHING = False
            self.update_status("⚠️  Something went wrong during installation.")
            messagebox.showerror("Error", str(e))
        finally:
            self.flash_btn.configure(state="normal")
            FLASHING = False

    def animate_progress(self, start, end):
        for i in range(start, end + 1):
            self.update_progress(i)
            time.sleep(0.01)


if __name__ == "__main__":
    # Ensure only one instance is running
    handle = ensure_single_instance(
        app_name="AMN_STM32_Flasher",
        window_title="AMN STM32 Flasher",
        focus_existing=True
    )

    try:
        # Start main GUI app
        app = FlasherApp()
        app.mainloop()
    finally:
        # Always release the instance lock on exit
        release_single_instance(handle)