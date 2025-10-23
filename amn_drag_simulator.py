# ----------------------------------------------------------------------
# AMN STM32 Flasher v1.0.0 – The First Drag-and-Drop Firmware Flasher
# ----------------------------------------------------------------------
# Copyright 2025 Aneesh Murali Nariyampully – Apache 2.0
# ----------------------------------------------------------------------
# Module: amn_drag_simulator.py
# Purpose:
#   Adds a transparent floating-text animation following the cursor
#   during drag operations to enhance user feedback.


import tkinter as tk
import ctypes

# Apply color-key transparency to a window.
def make_window_transparent(hwnd, color_key=(245, 245, 245)):  # ultra-light grey key
    user32 = ctypes.windll.user32
    LWA_COLORKEY = 0x00000001
    WS_EX_LAYERED = 0x00080000
    GWL_EXSTYLE = -20

    # Make window layered
    style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED)

    # Convert RGB to COLORREF (0x00BBGGRR)
    key_color = (color_key[2] << 16) | (color_key[1] << 8) | color_key[0]
    user32.SetLayeredWindowAttributes(hwnd, key_color, 0, LWA_COLORKEY)


class AMNDragSimulator:
    def __init__(self, app, widget, get_text_func, condition_func):
        self.app = app
        self.widget = widget
        self.get_text_func = get_text_func
        self.condition_func = condition_func

        self.tip = None
        self.alpha = 1.0
        self.fade_speed = 0.05
        self.dragging = False

        widget.bind("<ButtonPress-1>", self._on_press, add="+")
        widget.bind("<B1-Motion>", self._on_motion, add="+")
        widget.bind("<ButtonRelease-1>", self._on_release, add="+")

    def _on_press(self, event):
        if not self.condition_func():
            return
        text = self.get_text_func()
        if not text:
            return
        self.dragging = True
        self._create_floating_text(event.x_root, event.y_root, text)

    def _on_motion(self, event):
        if self.dragging and self.tip:
            self.tip.geometry(f"+{event.x_root + -20}+{event.y_root + -20}")

    def _on_release(self, event):
        if self.dragging:
            self.dragging = False
            if self.tip:
                self._fade_out()

    def _create_floating_text(self, x, y, text):
        if self.tip:
            try:
                self.tip.destroy()
            except Exception:
                pass

        self.tip = tk.Toplevel(self.app)
        self.tip.overrideredirect(True)
        self.tip.attributes("-topmost", True)
        self.tip.geometry(f"+{x + -20}+{y + -20}")

        bg_color = "#F5F5F5"  # ultra-light grey key color
        self.tip.configure(bg=bg_color)

        label = tk.Label(
            self.tip,
            text=text,
            font=("Helvetica", 16),
            fg="#fafafa",
            bg=bg_color,
            padx=8,
            pady=4,
        )
        label.pack()

        hwnd = self.tip.winfo_id()
        make_window_transparent(hwnd, color_key=(245, 245, 245))
        self.tip.attributes("-alpha", 1.0)

    def _fade_out(self):
        def step():
            if not self.tip:
                return
            self.alpha -= self.fade_speed
            if self.alpha <= 0:
                try:
                    self.tip.destroy()
                except Exception:
                    pass
                self.tip = None
                self.alpha = 1.0
                return
            self.tip.attributes("-alpha", self.alpha)
            self.app.after(int(1000 / 60), step)
        step()


# --- Demo ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("AMN Drag Simulator — Ultra-Light Grey Transparency")
    root.geometry("400x300")
    root.configure(bg="#202020")

    tk.Label(root, text="Drag any label below",
             fg="white", bg="#202020", font=("Segoe UI", 11)).pack(pady=15)

    items = ["Launch", "Files", "Settings", "Music", "Calendar"]

    for item in items:
        lbl = tk.Label(root, text=item, fg="white", bg="#333333",
                       font=("Segoe UI", 11), padx=16, pady=8, relief="ridge")
        lbl.pack(pady=4)

        AMNDragSimulator(
            root, lbl,
            get_text_func=lambda i=item: f"Dragging {i}",
            condition_func=lambda: True
        )

    root.mainloop()
