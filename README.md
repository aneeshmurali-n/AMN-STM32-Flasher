# AMN-STM32-Flasher

**AMN STM32 Flasher** is a one-click firmware flasher for STM32 microcontrollers.  
This app makes flashing STM32 microcontrollers **as easy as installing a regular application**. Simply place the compiled `.bin` firmware in the `bin` folder, share the app, and your users can:  

1. Connect their MCU to a PC.  
2. Run the app.  
3. Click **Install**.  

The firmware is automatically burned onto the chip — no source code, no code editor, no complex setup required.  

This tool is perfect for **beginners and non-experienced users**, allowing anyone to try out STM32 projects **without compiling code or setting up development environments**. It also **saves time for experienced embedded system engineers**, as everything is fully automated.

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
  ##### Folder Structure 
```text
AMN_STM32_Flasher/
├─ bin/
│  ├─ firmware.bin       # Your .bin firmware file
│  └─ settings.json      # Configuration file
└─ AMN STM32 Flasher.exe # Compiled executable
```

3. Double-click `AMN STM32 Flasher.exe` to launch.
   
- ⚠️ Make sure your `.bin` firmware is in the `bin` folder, and `ST-LINK_CLI.exe` is installed on your computer.
- It comes with **ST-LINK Utility**, or some **Arduino STM32 cores**.
- If you already have one of these installed, you’re ready to go.


---


## Usage

1. Launch **AMN STM32 Flasher**.  
2. The app will automatically detect `.bin` firmware files in the `bin` folder.  
3. If `ST-LINK_CLI.exe` is found, the **Install** button will be enabled.  
4. Optionally, check or uncheck **Enable Firmware Protection** to enable or disable RDP1 protection.  
5. Click **Install** to flash the firmware to your STM32 device.  
6. Monitor the **progress bar** and **status messages** for real-time feedback.

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

### For the App (Executable)

- Windows 10 or 11  
- **ST-LINK_CLI Requirement:** This software requires `ST-LINK_CLI.exe` from **official STMicroelectronics sources**.  
- Users must **obtain and install it separately** via one of the official packages:  
  - ST-LINK Utility  
  - Arduino STM32 cores that include it  

⚠️ **Important:** This repository **does not include `ST-LINK_CLI.exe`** due to **ST’s licensing restrictions**.  
You **do not need to copy or redistribute it**. The app will automatically detect `ST-LINK_CLI.exe` on your system and use it if it’s available, just like a person would. Make sure you have any of the ST programs installed (ST-LINK Utility, STM32F1xx board support via Arduino/STM32duino core).  

**Note:**  
- Do **not** copy `ST-LINK_CLI.exe` into the app folder. Doing so may **violate ST’s license**.  
- This is **your responsibility**, not the developer’s.  
- The app will automatically detect `ST-LINK_CLI.exe` if it’s installed on your system, so copying it is **not required**.  
- The author **recommends following ST’s license** and not redistributing the file.



### If Running from Source

- Python 3.12.5 or higher  
- Required Python packages:  
  - `customtkinter==5.2.2`  # For the user interface  


---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  


---

## Credits

- **Aneesh Murali Nariyampully** – Original author & developer  
- **CustomTkinter**  – MIT License (by Tom Schimansky)
- **STMicroelectronics** – `ST-LINK_CLI.exe` (used as a dependency, see licensing notes)  

---

## Disclaimer

- This software is provided “as-is” with **no warranty**.  
- The developer is **not responsible** for any firmware, hardware, or software issues caused by misuse, improper flashing, or license violations.  
- Users must comply with STMicroelectronics’ licensing terms if they use `ST-LINK_CLI.exe`.  
- Using this app assumes that the user understands and accepts all risks related to flashing STM32 devices.
