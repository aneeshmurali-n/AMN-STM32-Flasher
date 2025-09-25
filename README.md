# AMN-STM32-Flasher

**AMN STM32 Flasher** is a one-click firmware flasher for STM32 microcontrollers.  
It allows you to create a firmware installer for your STM32 projects with a user-friendly interface, automatic `.bin` file detection, and optional firmware protection (RDP1).  
Install firmware to your STM32 devices as easily as installing a regular application.

---

## Features

- **Easy Firmware Flashing** – Install firmware like a standard application.  
- **One-Click Automation** – Flash your device with a single button click.  
- **Automatic Firmware Detection** – Detects `.bin` firmware files in the `bin` folder automatically.  
- **ST-LINK Detection** – Searches for `ST-LINK_CLI.exe` in common system locations.  
- **Modern Dark UI** – Sleek dark mode interface with a purple-green theme.  
- **Optional Firmware Protection** – Enable or disable read protection (RDP1).  
- **Smooth Progress Feedback** – Real-time progress bar and status messages for every step.  

---

## Installation

1. **Download the latest release** from this repository.  
2. Ensure the following structure:  
AMN_STM32_Flasher/
├─ bin/
│ ├─ firmware.bin # Your .bin firmware file
│ └─ settings.json # Configuration file
└─ AMN STM32 Flasher.exe # Compiled executable
3. Double-click `AMN STM32 Flasher.exe` to launch.
   
> ⚠️ Make sure your `.bin` firmware is in the `bin` folder, and `ST-LINK_CLI.exe` is installed on your computer.  
> It comes with **STM32CubeProgrammer**, **ST-LINK Utility**, or some **Arduino STM32 cores**.  
> If you already have one of these installed, you’re ready to go.

---

## Usage

1. Launch **AMN STM32 Flasher**.  
2. The app will automatically detect `.bin` firmware files in the `bin` folder.  
3. If `ST-LINK_CLI.exe` is found, the **Install** button will be enabled.  
4. Optionally, check **Enable Firmware Protection** to enable RDP1 protection.  
5. Click **Install** to flash the firmware to your STM32 device.  
6. Monitor the **progress bar** and **status messages** for real-time feedback.

---

## Configuration (`bin/settings.json`)

Example:

```json
{
  "FLASH_START_ADDR": "0x08000000"
}

- FLASH_START_ADDR – Flash start address (usually 0x08000000 for STM32). You can change this according to your requirements.

---

## Requirements

### App

- Windows 10/11  
- `ST-LINK_CLI.exe` must be present on your system (from STMicroelectronics, comes with **STM32CubeProgrammer**, **ST-LINK Utility**, or some **Arduino STM32 cores**; not included in this repo due to licensing)

### If running from source

- Python 3.12.5  
- Packages:  
  - `customtkinter==5.2.2`

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

**Note:** `ST-LINK_CLI.exe` is **not redistributable**. Users must obtain it from STMicroelectronics separately.

---

## Credits

- **Aneesh Murali Nariyampully** – Original author & developer  
- **CustomTkinter** – MIT License  
- **STMicroelectronics** – `ST-LINK_CLI.exe` (used as a dependency, see licensing notes)  

---

## Disclaimer

- Use at your own risk.  
- Always verify the correct firmware and flash settings before proceeding.  
- The software is provided “as-is” with no warranty.
