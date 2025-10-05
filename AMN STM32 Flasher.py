# AMN STM32 Flasher
# Copyright 2025 Aneesh Murali Nariyampully
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import customtkinter as ctk
import subprocess
import time
from pathfinder import find_path
import json
from formatter import format_firmware_name
from theme import theme
from customtkinter.windows.widgets.theme import theme_manager
from binfinder import find_bin_file
import shutil
from tkinter import filedialog, messagebox
import threading
from zipper import zip_app_with_progress
from pathlib import Path


STLINK_CLI_PATH = None
FIRMWARE_FILE = None
FLASH_START_ADDR = "0x08000000"
CREATE_NO_WINDOW = 0x08000000
CACHE_FILE = "cache.amn"  # Cache file in the app directory



theme_Dark_Purple_Green_By_AMN = theme
# Inject the theme dictionary directly into CustomTkinter's ThemeManager
# so that all CTk widgets use this color palette from memory.
theme_manager.ThemeManager.theme = theme_Dark_Purple_Green_By_AMN

# Give this in-memory theme an internal name for reference.
theme_manager.ThemeManager._current_theme_name = "Dark_Purple_Green_By_AMN"


# --- Disable all file-based theme loading ---
# Prevent CustomTkinter from trying to open or read JSON theme files from disk.
# This ensures the app always uses the in-memory theme and avoids temporary files.
ctk.set_default_color_theme = lambda *a, **k: None
ctk.ThemeManager.load_theme = lambda *a, **k: None


# --- Safe fallback ---
# Attempt to "load" the in-memory theme name in case future CustomTkinter versions
# still require a load call. If it fails, silently ignore.
try:
    theme_manager.ThemeManager.load_theme("Dark_Purple_Green_By_AMN")
except Exception:
    pass


# --- Appearance Mode ---
# Set overall appearance mode (light/dark mode behavior for the theme).
ctk.set_appearance_mode("Dark")




class FlasherApp(ctk.CTk):
    def on_close(self):
        """Prevent accidental close while zipping; otherwise close normally."""
        if getattr(self, "zipping", False):
            if not messagebox.askyesno(
                    "Zipping in Progress",
                    "An installer is currently being created.\nClosing now will cancel the process.\n\nDo you really want to exit?"
            ):
                return
        self.destroy()

    def __init__(self):
        super().__init__()

        self.title("AMN STM32 Flasher")
        self.geometry("550x190")
        self.resizable(False, False)
        self.iconbitmap("assets/amnflasher.ico")

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

        # Start searching for ST-LINK_CLI.exe in background
        threading.Thread(target=self.locate_stlink, daemon=True).start()

        # Bind  keys to handle Keyboard Shortcut events
        self.bind("<Key-d>", self.handle_delete_key)
        self.bind("<Key-D>", self.handle_delete_key)  # also uppercase
        self.bind("<Delete>", self.handle_delete_key)
        self.bind("<Key-c>", self.handle_zip_key)
        self.bind("<Key-C>", self.handle_zip_key)
        self.bind("<Key-I>", self.handle_flash_key)
        self.bind("<Key-i>", self.handle_flash_key)
        self.bind("<Key-a>", self.handle_add_key)
        self.bind("<Key-A>", self.handle_add_key)
        self.bind("<Return>", self.handle_flash_key)  # <Return> is Enter
        self.bind("<KP_Enter>", self.handle_flash_key)  # Numpad Enter
        self.bind_all("<p>", self.handle_rdp_checkbox_key)
        self.bind_all("<P>", self.handle_rdp_checkbox_key)
        self.bind_all("<e>", self.handle_rdp_checkbox_key)
        self.bind_all("<E>", self.handle_rdp_checkbox_key)

    # ---------------- Settings ----------------
    def load_settings(self):
        global FLASH_START_ADDR
        settings_file = 'bin/settings.json'
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
            FLASH_START_ADDR = settings['FLASH_START_ADDR']
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            messagebox.showerror("Settings File Error", f"{str(e)}")
            self.destroy()


    # ---------------- Firmware Browse ----------------
    def browse_firmware(self):
        """Open file dialog to select firmware, copy to bin folder, and update button."""
        file_path = filedialog.askopenfilename(
            title="Select Firmware (.bin)",
            filetypes=[("Binary files", "*.bin")]
        )

        if not file_path:
            return  # user canceled

        bin_folder = Path("bin")
        bin_folder.mkdir(exist_ok=True)
        dest_path = bin_folder / Path(file_path).name
        shutil.copy(file_path, dest_path)

        global FIRMWARE_FILE
        FIRMWARE_FILE = dest_path.name

        # Update status and button (keep disabled until ST-LINK is found)
        self.update_status(f"Ready to install {format_firmware_name(FIRMWARE_FILE)}")
        self.flash_btn.configure(text="Install", state="normal", command=self.start_flash)


    def handle_delete_key(self, event):
        """Handle pressing 'D' key to delete firmware."""
        global FIRMWARE_FILE

        if not FIRMWARE_FILE:
            self.update_status("No firmware to delete!")
            return

        # Ask for confirmation
        confirm = messagebox.askokcancel(
            "Delete Firmware",
            f"Are you sure you want to delete {FIRMWARE_FILE}?"
        )
        if not confirm:
            return

        # Delete the firmware file
        try:
            firmware_path = Path("bin") / FIRMWARE_FILE
            if firmware_path.exists():
                firmware_path.unlink()
            FIRMWARE_FILE = None

            # Update UI
            self.update_status("Firmware deleted")
            self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete firmware:\n{str(e)}")

    # ---------------- Path Finder ----------------
    def locate_stlink(self):
        global STLINK_CLI_PATH, FIRMWARE_FILE
        self.update_status("Scanning for required files, please wait...")

        # Default search directory
        start_dirs = [r"C:\Program Files (x86)\STMicroelectronics\STM32 ST-LINK Utility\ST-LINK Utility"]

        # Check cache first
        cached_path = None
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "rb") as f:
                cached_path = f.read().decode("utf-8").strip()
            if cached_path and os.path.exists(cached_path):
                cached_dir = os.path.dirname(cached_path)
                if cached_dir not in start_dirs:
                    start_dirs.insert(0, cached_dir)

        # Find ST-LINK_CLI.exe
        STLINK_CLI_PATH = find_path("ST-LINK_CLI.exe", start_dirs=start_dirs)
        if STLINK_CLI_PATH is None:
            STLINK_CLI_PATH = find_path("ST-LINK_CLI.exe")  # full scan

        if STLINK_CLI_PATH:
            # Update cache
            if cached_path != STLINK_CLI_PATH:
                with open(CACHE_FILE, "wb") as f:
                    f.write(STLINK_CLI_PATH.encode("utf-8"))

            # Load settings for FLASH_START_ADDR
            self.load_settings()

            # Check for firmware
            FIRMWARE_FILE = find_bin_file(full_path=False)

            if not FIRMWARE_FILE:
                self.update_status("No firmware found in 'bin' folder!")
                self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
            else:
                self.update_status(f"Ready to install {format_firmware_name(FIRMWARE_FILE)}")
                self.flash_btn.configure(text="Install", state="normal", command=self.start_flash)
        else:
            self.update_status("Error: ST-LINK_CLI.exe not found on this computer!")
            self.flash_btn.configure(state="disabled")


    # ---------------- GUI Updates ----------------
    def update_status(self, text):
        self.after(0, lambda: self.status_label.configure(text=text))

    def update_progress(self, value):
        self.after(0, lambda: self.progress.set(value / 100))


    # ---------------- Flashing ----------------
    def start_flash(self):
        self.flash_btn.configure(state="disabled")
        threading.Thread(target=self.flash_firmware, daemon=True).start()

    def handle_flash_key(self,event):
        if self.flash_btn.cget("text").lower() == "install":
            self.start_flash()
        elif self.flash_btn.cget("text").lower() == "add firmware":
            self.browse_firmware()

    def handle_add_key(self,event):
        if self.flash_btn.cget("text").lower() == "add firmware":
            self.browse_firmware()

    def handle_rdp_checkbox_key(self, event):
        self.rdp_checkbox.toggle()




    def enable_rdp1(self):
        self.update_status("Enabling Protection...")
        try:
            result = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-OB", "RDP=1", "-Rst"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=CREATE_NO_WINDOW
            )
            if result.returncode != 0:
                raise RuntimeError(f"Failed to enable protection!\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
            self.update_status("Firmware protected.")
        except Exception as e:
            self.update_status("Failed to enable protection!")
            messagebox.showerror("Protection Error", f"Firmware flashed, but enabling protection was unsuccessful:\n{str(e)}")

    def flash_firmware(self):
        self.update_status("Initializing...")
        self.animate_progress(0, 10)

        if not Path(STLINK_CLI_PATH).exists():
            messagebox.showerror("Error", f"ST-LINK_CLI not found: {STLINK_CLI_PATH}")
            self.flash_btn.configure(state="normal")
            self.update_status("Please resolve the issue and try again.")
            self.update_progress(0)
            return

        firmware_path = Path("bin/" + FIRMWARE_FILE)
        if not firmware_path.exists():
            messagebox.showerror("Error", f"Firmware file not found: {firmware_path}")
            self.flash_btn.configure(state="normal")
            self.update_status("Please resolve the issue and try again.")
            self.update_progress(0)
            self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
            return

        try:
            # Disable RDP
            self.update_status("Disabling Protection...")
            result_erase = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-OB", "RDP=0", "-Rst"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=CREATE_NO_WINDOW
            )
            if result_erase.returncode != 0:
                raise RuntimeError(f"Operation failed!\n{result_erase.stdout}\n{result_erase.stderr}")
            self.animate_progress(10, 35)

            # Full chip erase
            self.update_status("Performing full chip erase...")
            result_erase = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-ME", "-Rst"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=CREATE_NO_WINDOW
            )
            if result_erase.returncode != 0:
                raise RuntimeError(f"Operation failed!\n{result_erase.stdout}\n{result_erase.stderr}")
            self.animate_progress(35, 50)

            # Flash firmware
            self.update_status("Installing firmware...")
            result_flash = subprocess.run(
                [STLINK_CLI_PATH, "-c", "SWD", "-P", str(firmware_path), FLASH_START_ADDR, "-Rst"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=CREATE_NO_WINDOW
            )
            if result_flash.returncode != 0:
                raise RuntimeError(f"Installation failed!\n{result_flash.stdout}\n{result_flash.stderr}")
            self.animate_progress(50, 100)

            if self.rdp_var.get():
                self.enable_rdp1()

            self.update_progress(100)
            self.update_status("Firmware installed successfully!")

        except Exception as e:
            self.update_status("Installation failed!")
            messagebox.showerror("Error", str(e))
        finally:
            self.flash_btn.configure(state="normal")

    def animate_progress(self, start, end):
        for i in range(start, end + 1):
            self.update_progress(i)
            time.sleep(0.01)


# ---------------- Zipping ----------------
    def handle_zip_key(self, event):
        """Zip entire app directory with progress animation."""
        global FIRMWARE_FILE
        if not FIRMWARE_FILE:
            self.update_status("⚠️ Please add firmware before creating an installer.")
            messagebox.showwarning("No Firmware Found", "Please add a firmware before creating an installer.")
            return
        folder = filedialog.askdirectory(title=f"Choose where to save the {format_firmware_name(FIRMWARE_FILE)} installer")
        if not folder:
            return

        self.update_status(f"Creating installer package for {format_firmware_name(FIRMWARE_FILE)}...")
        self.flash_btn.configure(state="disabled")

        def progress_callback(value):
            """Update progress bar from zipper."""
            self.update_progress(value)

        def zip_thread():
            # mark busy and protect close on main thread
            self.zipping = True
            self.after(0, lambda: self.protocol("WM_DELETE_WINDOW", self.on_close))

            try:
                result = zip_app_with_progress(app_dir=".", bin_folder="bin", progress_callback=progress_callback)

                if result is None:
                    # no firmware
                    self.after(0, lambda: [
                        self.update_status("No firmware found in bin folder!"),
                        self.flash_btn.configure(text="Add Firmware", state="normal", command=self.browse_firmware)
                    ])
                    return

                if isinstance(result, str) and result.startswith("missing_legal"):
                    missing = result.split(":", 1)[1]
                    self.after(0, lambda: [
                        messagebox.showerror("Files Missing!", f"Missing the following required files: {missing}"),
                        self.update_status(f"Missing required files: {missing}")
                    ])
                    return

                # success: result is (zip_bytes, firmware_name)
                zip_bytes, firmware_name = result

                final_zip_path = Path(folder) / f"{firmware_name}.zip"
                tmp_path = final_zip_path.with_name(final_zip_path.name + ".part")

                try:
                    with open(tmp_path, "wb") as f:
                        f.write(zip_bytes)
                    tmp_path.replace(final_zip_path)  # atomic replace on same filesystem
                except Exception as e:
                    # write error
                    self.after(0, lambda: messagebox.showerror("Installer Error", f"Failed to save installer:\n{e}"))
                    try:
                        if tmp_path.exists():
                            tmp_path.unlink()
                    except Exception:
                        pass
                    return

                # success UI
                self.after(0, lambda: self.update_status(
                    f"{format_firmware_name(FIRMWARE_FILE)} installer created!\nLocation: {final_zip_path}"))

            except Exception as e:
                self.after(0, lambda: messagebox.showerror("Installer Error", f"Failed to create installer:\n{e}"))

            finally:
                # restore UI & protocol on main thread
                self.zipping = False
                self.after(0, lambda: self.protocol("WM_DELETE_WINDOW", self.on_close))
                self.after(0, lambda: self.flash_btn.configure(state="normal"))
                self.update_progress(0)

        threading.Thread(target=zip_thread, daemon=True).start()


if __name__ == "__main__":
    app = FlasherApp()
    app.mainloop()
