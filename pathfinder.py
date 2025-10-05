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
