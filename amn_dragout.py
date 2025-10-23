# ----------------------------------------------------------------------
# AMN STM32 Flasher v1.0.0 – The First Drag-and-Drop Firmware Flasher
# ----------------------------------------------------------------------
# Copyright 2025 Aneesh Murali Nariyampully – Apache 2.0
# ----------------------------------------------------------------------
# Module: amn_dragout.py
# Purpose:
#   Detects when a file is dragged outside the app window and triggers
#   safe firmware removal from workspace or UI reset.

import time
import threading

# Enables a drag-out gesture for the given widget.
# When the user:
    # 1. Clicks and holds on the widget,
    # 2. Drags the cursor outside the app window, and
    # 3. Releases the mouse button,
    # then `callback()` is executed.

    # Args:
    # widget: The Tkinter/CustomTkinter widget to watch.
    # callback: Function to call when drag-out is detected.

def enable_amn_drag_out(widget, callback):
    state = {
        "dragging": False,
        "press_time": 0.0,
    }

    def on_press(event):
        state["dragging"] = True
        state["press_time"] = time.time()
        try:
            widget.configure(cursor="hand2")
        except Exception:
            pass

    def on_release(event):
        try:
            widget.configure(cursor="")
        except Exception:
            pass

        if not state["dragging"]:
            return
        state["dragging"] = False

        # Prevent accidental click
        if time.time() - state["press_time"] < 0.05:
            return

        try:
            top = widget.winfo_toplevel()
            wx, wy = top.winfo_rootx(), top.winfo_rooty()
            ww, wh = top.winfo_width(), top.winfo_height()
            rx, ry = event.x_root, event.y_root

            # Detect if cursor released outside window bounds
            outside = rx < wx or ry < wy or rx > wx + ww or ry > wy + wh

            if outside:
                # Run callback on main thread
                widget.after(0, callback)
        except Exception:
            # Fallback in case of Tk issues
            threading.Thread(target=callback, daemon=True).start()

    widget.bind("<ButtonPress-1>", on_press, add="+")
    widget.bind("<ButtonRelease-1>", on_release, add="+")
