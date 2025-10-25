# ----------------------------------------------------------------------
# AMN STM32 Flasher v1.0.0
# The world’s first flashing app that makes flashing as easy as moving a file.
# ----------------------------------------------------------------------
# Copyright 2025 Aneesh Murali Nariyampully
# Licensed under the Apache License, Version 2.0
# ----------------------------------------------------------------------
# Module: amn_instance.py
# Purpose:
#   Ensures only one instance of AMN STM32 Flasher runs at a time and
#   brings the existing window to the foreground if re-launched.
# ----------------------------------------------------------------------
# Legal Notice:
#   Requires ST-LINK Utility & drivers installed separately.
#   No STMicroelectronics property is included or modified.



import ctypes
import sys

# Windows API constants
ERROR_ALREADY_EXISTS = 183
SW_RESTORE = 9

# ctypes Win32 bindings
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
user32 = ctypes.WinDLL("user32", use_last_error=True)

# Function signatures
kernel32.CreateMutexW.argtypes = [ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p]
kernel32.CreateMutexW.restype = ctypes.c_void_p

kernel32.ReleaseMutex.argtypes = [ctypes.c_void_p]
kernel32.ReleaseMutex.restype = ctypes.c_bool

kernel32.CloseHandle.argtypes = [ctypes.c_void_p]
kernel32.CloseHandle.restype = ctypes.c_bool

user32.FindWindowW.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p]
user32.FindWindowW.restype = ctypes.c_void_p

user32.ShowWindow.argtypes = [ctypes.c_void_p, ctypes.c_int]
user32.ShowWindow.restype = ctypes.c_bool

user32.SetForegroundWindow.argtypes = [ctypes.c_void_p]
user32.SetForegroundWindow.restype = ctypes.c_bool


def ensure_single_instance(app_name="AMN_STM32_Flasher", window_title=None, focus_existing=True):

    # Prevents multiple instances of the app from running.
    # If another instance is detected, optionally focuses its window and exits.
    # Returns a handle to the mutex if this is the first instance.

    mutex_name = f"Global\\{app_name}_Mutex"

    # Create named mutex
    handle = kernel32.CreateMutexW(None, False, mutex_name)

    # Check if already exists
    last_error = ctypes.get_last_error()
    if last_error == ERROR_ALREADY_EXISTS:
        if focus_existing and window_title:
            try:
                hwnd = user32.FindWindowW(None, window_title)
                if hwnd:
                    user32.ShowWindow(hwnd, SW_RESTORE)
                    user32.SetForegroundWindow(hwnd)
            except Exception:
                pass
        # Another instance is running, exit immediately
        sys.exit(0)

    return handle


def release_single_instance(handle):

    # Releases the named mutex created by ensure_single_instance().
    # Call this at the end of your program.

    try:
        if handle:
            kernel32.ReleaseMutex(handle)
            kernel32.CloseHandle(handle)
    except Exception:
        pass

