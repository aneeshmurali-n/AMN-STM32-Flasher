# ----------------------------------------------------------------------
# AMN STM32 Flasher v1.0.0 – The First Drag-and-Drop Firmware Flasher
# ----------------------------------------------------------------------
# Copyright 2025 Aneesh Murali Nariyampully – Apache 2.0
# ----------------------------------------------------------------------
# Module: pathfinder.py
# Purpose:
#   Searches for ST-LINK_CLI.exe across drives and caches its path for
#   faster startup and reliable CLI access.



import os
from pathlib import Path
import string

# Return all available drives on Windows.
def get_drives():
    return [f"{d}:\\" for d in string.ascii_uppercase if Path(f"{d}:\\").exists()]

def find_path(filename, start_dirs=None):
    # Search for a file, checking the current directory first, then optional directories, then all drives.

    # :param filename: Name of the file to search for (e.g., "ST-LINK_CLI.exe")
    # :param start_dirs: Optional list of directories to search before scanning all drives
    # :return: Full path to the first match, or None if not found

    # 1. Check current working directory first
    cwd_path = Path(os.getcwd()) / filename
    if cwd_path.exists():
        return str(cwd_path.resolve())

    # 2. Check additional directories if provided
    if start_dirs:
        for directory in start_dirs:
            search_path = Path(directory) / filename
            if search_path.exists():
                return str(search_path.resolve())

    # 3. Fallback to all drives (Windows only)
    if start_dirs is None:
        start_dirs = get_drives()

    for drive in start_dirs:
        for root, dirs, files in os.walk(drive):
            try:
                if filename in files:
                    return str(Path(root) / filename)
            except PermissionError:
                continue

    # Not found
    return None

# Example usage
if __name__ == "__main__":
    file_to_find = "ST-LINK_CLI.exe"
    path = find_path(file_to_find)
    if path:
        print(f"Found {file_to_find} at: {path}")
    else:
        print(f"{file_to_find} not found on this PC.")
