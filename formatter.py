# ----------------------------------------------------------------------
# AMN STM32 Flasher v1.0.0
# The world’s first flashing app that makes flashing as easy as moving a file.
# ----------------------------------------------------------------------
# Copyright 2025 Aneesh Murali Nariyampully – Apache 2.0
# ----------------------------------------------------------------------
# Module: formatter.py
# Purpose:
#   Converts firmware filenames into clean, readable labels
# Examples:
# - "AMN_CLI_Timer_v1_0_0.bin" -> "AMN CLI Timer v1.0.0"
# - "AMN_CLI_Timer_v1_0.bin" -> "AMN CLI Timer v1.0"
# - "Driver_v3_2.bin" -> "Driver v3.2"
# ----------------------------------------------------------------------

import re


def format_firmware_name(filename: str) -> str:
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

