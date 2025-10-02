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
