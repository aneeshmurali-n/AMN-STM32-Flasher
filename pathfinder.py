"""
MIT License

Copyright (c) 2025 Aneesh Murali Nariyampully

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from pathlib import Path
import string

def get_drives():
    """Return all available drives on Windows."""
    return [f"{d}:\\" for d in string.ascii_uppercase if Path(f"{d}:\\").exists()]

def find_path(filename, start_dirs=None):
    """
    Search for a file, checking the current directory first, then optional directories, then all drives.

    :param filename: Name of the file to search for (e.g., "ST-LINK_CLI.exe")
    :param start_dirs: Optional list of directories to search before scanning all drives
    :return: Full path to the first match, or None if not found
    """
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
