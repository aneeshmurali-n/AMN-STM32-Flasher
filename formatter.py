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


import re


def format_firmware_name(filename: str) -> str:
    """
    Convert a firmware filename into a human-readable format.

    Examples:
    - "AMN_CLI_Timer_v1_0_0.bin" -> "AMN CLI Timer v1.0.0"
    - "AMN_CLI_Timer_v1_0.bin" -> "AMN CLI Timer v1.0"
    - "Driver_v3_2.bin" -> "Driver v3.2"
    """
    # Remove file extension
    name = re.sub(r'\.bin$', '', filename, flags=re.IGNORECASE)

    # Replace underscores with spaces
    name = name.replace('_', ' ')

    # Format version: v1 0 0 -> v1.0.0, v1 0 -> v1.0
    formatted_name = re.sub(
        r'v(\d+(?: \d+)*)',
        lambda m: 'v' + '.'.join(m.group(1).split()),
        name
    )

    return formatted_name


# Example run when this file is executed directly
if __name__ == "__main__":
    # Example firmware filenames
    firmware_examples = [
        "AMN_CLI_Timer_v1_0_0.bin",
        "AMN_CLI_Timer_v1_0.bin",
        "Sensor_Module_v2_5_3.bin",
        "Bootloader_v0_9_12.bin",
        "Driver_v3_2.bin",
        "hello 123",
        "hello v1.0.1004"
    ]

    print("Example Run of firmware_formatter.py\n")
    for f in firmware_examples:
        formatted = format_firmware_name(f)
        print(f"Original: {f} -> Formatted: {formatted}")
