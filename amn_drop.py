# ----------------------------------------------------------------------
# AMN STM32 Flasher v1.0.0
# The world’s first flashing app that makes flashing as easy as moving a file.
# ----------------------------------------------------------------------
# Copyright 2025 Aneesh Murali Nariyampully – Apache 2.0 License
# ----------------------------------------------------------------------
# Module: amn_drop.py
# Purpose:
#   Provides native Windows drag-and-drop integration so users can
#   drop .bin firmware files directly into the application window.
# ----------------------------------------------------------------------
# Legal Notice:
# Communicates externally with ST-LINK CLI, does not bundle it.



import ctypes
from ctypes import wintypes
import sys
DEBUGGING = False
WM_DROPFILES = 0x0233

# --- Fix missing types in Python 3.13+ / 3.14 ---
if not hasattr(wintypes, "LRESULT"):
    wintypes.LRESULT = wintypes.LPARAM
if not hasattr(wintypes, "UINT_PTR"):
    wintypes.UINT_PTR = ctypes.c_size_t
if not hasattr(wintypes, "DWORD_PTR"):
    wintypes.DWORD_PTR = ctypes.c_size_t

# --- Load DLLs ---
user32 = ctypes.WinDLL("user32", use_last_error=True)
shell32 = ctypes.WinDLL("shell32", use_last_error=True)
comctl32 = ctypes.WinDLL("comctl32", use_last_error=True)

# --- Function prototypes ---
DragAcceptFiles = shell32.DragAcceptFiles
DragQueryFile = shell32.DragQueryFileW
DragFinish = shell32.DragFinish

SUBCLASSPROC = ctypes.WINFUNCTYPE(
    wintypes.LRESULT,
    wintypes.HWND,
    wintypes.UINT,
    wintypes.WPARAM,
    wintypes.LPARAM,
    wintypes.UINT_PTR,
    wintypes.DWORD_PTR,
)

SetWindowSubclass = comctl32.SetWindowSubclass
SetWindowSubclass.argtypes = [
    wintypes.HWND,
    SUBCLASSPROC,
    wintypes.UINT_PTR,
    wintypes.DWORD_PTR,
]
SetWindowSubclass.restype = wintypes.BOOL

DefSubclassProc = comctl32.DefSubclassProc
DefSubclassProc.argtypes = [
    wintypes.HWND,
    wintypes.UINT,
    wintypes.WPARAM,
    wintypes.LPARAM,
]
DefSubclassProc.restype = wintypes.LRESULT


# ----------------------------------------------------------------
# Mixin class
# ----------------------------------------------------------------
# Adds native Windows drag-and-drop support to any Tk/CTk window.
class AMNDropMixin:
    # Enable drag-and-drop file receiving.
    def enable_drop(self, callback):
        self.update_idletasks()
        hwnd = self.winfo_id()
        DragAcceptFiles(hwnd, True)
        self._drop_callback = callback

        @SUBCLASSPROC
        def subclass_proc(hWnd, msg, wParam, lParam, uIdSubclass, dwRefData):
            if msg == WM_DROPFILES:
                try:
                    # Cast wParam to HANDLE to avoid OverflowError
                    hDrop = ctypes.c_void_p(wParam)

                    count = DragQueryFile(hDrop, 0xFFFFFFFF, None, 0)
                    files = []
                    for i in range(count):
                        length = DragQueryFile(hDrop, i, None, 0) + 1
                        buf = ctypes.create_unicode_buffer(length)
                        DragQueryFile(hDrop, i, buf, length)
                        files.append(buf.value)

                    DragFinish(hDrop)

                    if files and self._drop_callback:
                        self._drop_callback(files)
                except Exception as e:
                    if DEBUGGING : print("[AMNDropMixin] Drop error:", e, file=sys.stderr)
                return 0

            try:
                return DefSubclassProc(hWnd, msg, wParam, lParam)
            except Exception as e:
                if DEBUGGING : print("[AMNDropMixin] DefSubclassProc error:", e, file=sys.stderr)
                return 0

        # Keep a reference to prevent GC
        self._amn_subclass_proc = subclass_proc

        # Register subclass safely
        if not SetWindowSubclass(hwnd, self._amn_subclass_proc, 1001, 0):
            raise ctypes.WinError(ctypes.get_last_error())

