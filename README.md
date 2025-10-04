# AMN STM32 Flasher
<img width="1920" height="1080" alt="exp_1 1 1" src="https://github.com/user-attachments/assets/6970617b-b619-4b57-960d-ee9d183b4b93" />



**AMN STM32 Flasher** is a one-click firmware flasher for STM32 microcontrollers.  
It makes flashing STM32 devices **as easy as installing a regular application**. Simply place the compiled `.bin` firmware in the `bin` folder, share the app, and your users can:

1. Connect their MCU to a PC.  
2. Run the app.  
3. Click **Install**.  

The firmware is automatically burned onto the chip — no source code, no code editor, and no complex setup required.  

This tool is perfect for **beginners and non-experienced users**, allowing anyone to try out STM32 projects **without compiling code or setting up development environments**. It also **saves time for experienced embedded system engineers**, as everything is fully automated.

---

## ✨ Features
- **Easy Firmware Flashing** – Install firmware as easily as a standard application.  
- **One-Click Flash** – Flash your device with a single click.  
- **Create Firmware Installer** – Package your firmware as a single-click installer.  
- **Automatic Firmware Detection** – Detects `.bin` firmware files in the `bin` folder automatically.  
- **ST-LINK_CLI Automatic Detection** – Detects and uses `ST-LINK_CLI.exe` installed on your system.  
- **Modern Dark UI** – Sleek dark mode interface with a purple-green theme.  
- **Optional Firmware Protection** – Enable/disable read protection (RDP1).  
- **Smooth Progress Feedback** – Real-time progress bar and status updates.  
- **Keyboard Shortcuts** – Quickly access key functions without using the mouse.  

## ⌨️ Keyboard Shortcuts

| Shortcut       | Action                                   |
|----------------|------------------------------------------|
| `D` / `Delete` | 🗑️ Delete added firmware file            |
| `C`            | 📦 Create firmware installer             |
| `I` / `Enter`  | ⚡ Flash firmware                        |
| `A` / `Enter`  | ➕ Add firmware file                     |
| `P` / `E`      | 🔒 Enable / Disable Read Protection (RDP1) |


---

## How It Works

<img width="755" height="389" alt="Screenshot 2025-10-02 233050" src="https://github.com/user-attachments/assets/383ebed1-d129-4bfb-8916-8acf0879dec0" />

1. Click Add Firmware or press `A` / `Enter` on key board to add the `.bin` firmware in the `bin` folder.

<img width="1220" height="506" alt="Screenshot 2025-10-02 233123" src="https://github.com/user-attachments/assets/0a410f1e-960d-4f8a-9d92-1f7904f7b2b7" />

2. Browse your firmware file.

<img width="756" height="370" alt="Screenshot 2025-10-02 233142" src="https://github.com/user-attachments/assets/d2515af3-14f4-4cf8-ae88-6f44462a25ba" />

3. Connect your STM32 MCU to your PC via **ST-Link V2**.



4. (Optional) Check **Enable Firmware Protection** if you want to enable read protection (RDP1).

<img width="806" height="416" alt="image" src="https://github.com/user-attachments/assets/d9580073-a57d-496c-89dc-b6577f6dba65" />

   
5. Click **Install**.

<img width="822" height="463" alt="image" src="https://github.com/user-attachments/assets/f62a9a72-1cfe-4e28-815c-67b5d8a25797" />
   
The firmware will be flashed automatically with **real-time progress updates**.  

<img width="748" height="393" alt="image" src="https://github.com/user-attachments/assets/003a6774-80a8-4b45-bcdc-a46bd91d11b9" />


You can also share this app along with your `.bin` file in the `bin` folder. It works like a **package installer**, allowing someone else to flash the MCU with **just one click**.

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
- FLASH_START_ADDR – Flash start address (usually 0x08000000 for STM32). Adjust as needed.

---


## Requirements

### Running the Executable

- Windows 10 or 11  
- Installed ST-LINK_CLI.exe (via ST-LINK Utility or STM32 Arduino cores)

### Running from Source

- Python 3.12.5 or higher  
- Required Python packages:  
  - `customtkinter==5.2.2` 


---

## Why Use This App?

- Turn your firmware into a **sharable installer** for easy distribution.  
- Perfect for beginners who don’t want to deal with code editors or compilation.  
- Saves time for experienced embedded engineers with fully automated flashing.  
- Makes STM32 projects **accessible and easy to try** for anyone following tutorials or using shared firmware packages.
  
---

## Credits
- Aneesh Murali Nariyampully – Original author & developer  
- CustomTkinter – MIT License (by Tom Schimansky)  
- STMicroelectronics – ST-LINK_CLI.exe (dependency, see Important Notice)

---

## 📄 License

© 2025 Aneesh Murali Nariyampully  
Licensed under the Apache License, Version 2.0.  
You may obtain a copy of the License at  
[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an **"AS IS" BASIS**,  
**without warranties or conditions of any kind**, either express or implied.  
See the [LICENSE](LICENSE) file for full terms.

---

## Disclaimer

- This software is provided “as is”, without warranty of any kind.  
- The developer is not responsible for any hardware or firmware damage caused by misuse.  
- `ST-LINK_CLI.exe` is property of **STMicroelectronics** and must be used according to their license terms.

---


  
