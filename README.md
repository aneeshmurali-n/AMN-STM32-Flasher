# AMN STM32 Flasher

**AMN STM32 Flasher** is a one-click firmware flasher for STM32 microcontrollers.  
It makes flashing STM32 devices **as easy as installing a regular application**. Simply place the compiled `.bin` firmware in the `bin` folder, share the app, and your users can:

1. Connect their MCU to a PC.  
2. Run the app.  
3. Click **Install**.  

The firmware is automatically burned onto the chip — no source code, no code editor, and no complex setup required.  

This tool is perfect for **beginners and non-experienced users**, allowing anyone to try out STM32 projects **without compiling code or setting up development environments**. It also **saves time for experienced embedded system engineers**, as everything is fully automated.

---

## Features

- **Easy Firmware Flashing** – Install firmware as easily as a standard application.  
- **One-Click Flash** – Flash your device with a single click.  
- **Automatic Firmware Detection** – Automatically detects `.bin` firmware files in the `bin` folder.  
- **ST-LINK_CLI Automatic Detection** – Automatically finds and uses `ST-LINK_CLI.exe` installed on your system.  
- **Modern Dark UI** – Sleek dark mode interface with a purple-green theme.  
- **Optional Firmware Protection** – Enable or disable read protection (RDP1) to lock the microcontroller.  
- **Smooth Progress Feedback** – Real-time progress bar and status messages for every step.

---

## How It Works

1. Place the `.bin` firmware in the `bin` folder.  
2. Connect your STM32 MCU to your PC via **ST-Link V2**.
3. Run the app.
4. (Optional) Check **Enable Firmware Protection** to enable read protection (RDP1).  
5. Click **Install**.  

**The firmware will be flashed automatically, with real-time progress updates displayed during the process.  
You can also share this app along with your `.bin` firmware file placed in the `bin` folder. It now works like a **package installer**, allowing someone else to flash the MCU and try the project with just one click.**


---


## Dependencies & Licensing

- `ST-LINK_CLI.exe` from **STMicroelectronics** is required to flash STM32 devices.  
  - The app **does not include or redistribute** this executable, it must be installed on your system.  
  - See **Important Notice** below for licensing information.

---

## Important Notice

⚠️ **ST-LINK_CLI.exe is not included** due to ST’s licensing restrictions.  

- You **do not need to copy or redistribute** it. The app will detect it automatically if installed.  
- Copying `ST-LINK_CLI.exe` into the app folder **may violate ST’s license**. This is **your responsibility**, not the developer’s.  
- Ensure that one of the supported ST programs is installed:  
  - ST-LINK Utility  
  - Arduino STM32 cores (STM32F1xx/GD32F1xx boards by stm32duino)  

The app is designed to work without copying files, so **please comply with ST’s license**.

---

## Configuration (`bin/settings.json`)

Example:

```json
{
  "FLASH_START_ADDR": "0x08000000"
}
```
- FLASH_START_ADDR – Flash start address (usually 0x08000000 for STM32). You can change this according to your requirements.

---


## Requirements

### Running the Executable

- Windows 10 or 11  
- Installed ST-LINK_CLI.exe (via ST-LINK Utility or STM32 Arduino cores)

### Running from Source

- Python 3.12.5 or higher  
- Required Python packages:  
  - `customtkinter==5.2.2`  # For the user interface  


---

## Why Use This App?

- Perfect for beginners who don’t want to deal with code editors or compilation.  
- Saves time for experienced embedded engineers with fully automated flashing.  
- Makes STM32 projects **accessible and easy to try** for anyone watching tutorials or using shared firmware packages.
  
---

## Credits

- **Aneesh Murali Nariyampully** – Original author & developer  
- **CustomTkinter** – MIT License (by Tom Schimansky)  
- **STMicroelectronics** – ST-LINK_CLI.exe (used as a dependency, see Important Notice)
---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

---

## Disclaimer

- This software is provided “as-is” with **no warranty**.  
- The developer is **not responsible** for any firmware, hardware, or software issues caused by misuse, improper flashing, or license violations.  
- Users must comply with STMicroelectronics’ licensing terms if they use `ST-LINK_CLI.exe`.  
- Using this app assumes that the user understands and accepts all risks related to flashing STM32 devices.

---
  
