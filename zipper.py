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

import zipfile
import io
from pathlib import Path
from formatter import format_firmware_name

def zip_app_with_progress(app_dir: str = ".", bin_folder: str = "bin", progress_callback=None):
    """
    Create a ZIP archive entirely in memory and return (zip_bytes, firmware_name).
    Returns:
        (bytes, firmware_name): Success
        "missing_legal:..."   : LICENSE/NOTICE missing
        None                  : No firmware found
    """
    app_dir = Path(app_dir).resolve()
    bin_path = app_dir / bin_folder

    # --- Legal files check ---
    license_file = app_dir / "LICENSE.txt"
    notice_file = app_dir / "NOTICE.txt"

    missing_legal = []
    if not license_file.exists():
        missing_legal.append("LICENSE")
    if not notice_file.exists():
        missing_legal.append("NOTICE")

    if missing_legal:
        return f"missing_legal:{','.join(missing_legal)}"

    # --- Firmware check ---
    firmware_files = list(bin_path.glob("*.bin"))
    if not firmware_files:
        return None

    firmware_name = format_firmware_name(firmware_files[0].stem)

    # --- Create ZIP in RAM ---
    zip_buffer = io.BytesIO()
    files_to_zip = list(app_dir.rglob("*"))
    total_files = len(files_to_zip) or 1

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for idx, file in enumerate(files_to_zip, start=1):
            if file.suffix == ".zip" or file.name == "cache.amn":
                continue
            zipf.write(file, arcname=file.relative_to(app_dir))

            if progress_callback:
                progress = int((idx / total_files) * 100)
                progress_callback(progress)

    zip_buffer.seek(0)
    return zip_buffer.read(), firmware_name
