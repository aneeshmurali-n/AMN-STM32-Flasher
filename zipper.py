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
import zipfile
from pathlib import Path
from formatter import format_firmware_name
def zip_app_with_progress(app_dir: str = ".", bin_folder: str = "bin", progress_callback=None) -> str | None:
    """
    Zip the app directory if a firmware exists in bin folder, with progress callback.

    Args:
        app_dir (str): App directory (default current).
        bin_folder (str): Folder containing firmware (default 'bin').
        progress_callback (callable): Function(progress: int) to update progress (0-100).

    Returns:
        str | None: Path to zip file if created, None if no firmware found.
    """
    app_dir = Path(app_dir).resolve()
    bin_path = app_dir / bin_folder

    firmware_files = list(bin_path.glob("*.bin"))
    if not firmware_files:
        return None

    firmware_name = format_firmware_name(firmware_files[0].stem)
    zip_path = app_dir / f"{firmware_name}.zip"

    files_to_zip = list(app_dir.rglob("*"))
    total_files = len(files_to_zip)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for idx, file in enumerate(files_to_zip, start=1):
            if file == zip_path or file.name == "cache.amn":   # skip cache.amn file
                continue
            zipf.write(file, arcname=file.relative_to(app_dir))
            if progress_callback:
                progress = int((idx / total_files) * 100)
                progress_callback(progress)

    return str(zip_path)
