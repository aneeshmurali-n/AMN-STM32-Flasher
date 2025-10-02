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
