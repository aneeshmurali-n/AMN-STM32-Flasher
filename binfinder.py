# AMN STM32 Flasher
# binfinder.py — Locates firmware .bin files in the bin directory and return the first one found.
# Note:
#   This module is not currently used in the main application but is
#   retained for potential future use or feature expansion.
#
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


from pathlib import Path

def find_bin_file(bin_folder="bin", full_path=False):
    """
    Search for .bin files in the bin folder and return the first one found.

    :param bin_folder: Folder to search in (default "bin")
    :param full_path: If True, return absolute path; if False, return filename with extension
    :return: Full path or filename with extension of the first .bin file, or None if not found
    """
    bin_path = Path(bin_folder)
    if not bin_path.exists() or not bin_path.is_dir():
        return None

    bin_files = list(bin_path.glob("*.bin"))
    if bin_files:
        file = bin_files[0]
        if full_path:
            return str(file.resolve())  # Full absolute path
        else:
            return file.name  # Filename with extension

    return None


# Example usage
if __name__ == "__main__":
    print("Filename with extension:", find_bin_file(full_path=False))
    print("Full path:", find_bin_file(full_path=True))

