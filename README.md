# AMN STM32 Flasher  
![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.14%2B-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows_10/11-lightgrey.svg)
![UI](https://img.shields.io/badge/UI_Dark_purple_green_by_AMN-CustomTkinter-9cf.svg)
## 🏆 The World’s First Drag-and-Drop Firmware Flasher

**No terminals. No setup. No stress.**  
Just **drop your file** — and watch your STM32 flash itself.

Flashing STM32 firmware has never been this simple.  
**AMN STM32 Flasher** replaces command lines and scripts with a single action:  
**drag and drop** your `.bin` file — the app detects your ST-LINK, erases memory,  
installs, verifies, and protects your firmware automatically.

Built for developers, engineers, and makers who value **speed**, **clarity**, and **style**.  
Everything just works  beautifully.

---

## 🚀 Key Features

| ✨ Feature | 💡 Description |
|------------|----------------|
| 🖱️ **Drag & Drop Flashing** | Drop your `.bin` firmware file directly into the window — AMN handles everything. |
| ⚡ **Drop Flash Mode** | Enable instant auto-flash — your STM32 flashes the moment you drop a file. |
| 🧠 **Smart ST-LINK Detection** | Automatically locates `ST-LINK_CLI.exe` across drives and caches its path. |
| 🔒 **Firmware Protection (RDP)** | Enable or disable STM32 readout protection (RDP) with one click. |
| 🎛️ **Smooth Live Feedback** | 60 FPS animated progress bar with live status updates at every stage. |
| 🧩 **Single-Instance Engine** | Prevents multiple launches — focuses the current window intelligently. |
| 🪟 **True Native Integration** | Built natively for Windows with authentic drag-and-drop behavior. |
| 🎨 **Dark Modern Theme** | Custom **Dark Purple Green by AMN** theme for focus and visual comfort. |
| ⌨️ **Keyboard Shortcuts** | Quickly access key functions without using the mouse | 

 
---

## ⌨️ Keyboard Shortcuts

| Shortcut       | Action                                   |
|----------------|------------------------------------------|
| `Q`            | ⚡ Enable / Disable Drop Flash Mode      |
| `D` / `Delete` | 🗑️ Remove firmware file from workspace   |
| `I` / `Enter`  | ⚡ Flash firmware                        |
| `A` / `Enter`  | ➕ Add firmware file                     |
| `P` / `E`      | 🔒 Enable / Disable Read Protection (RDP1) |



---

## How It Works

<img width="755" height="389" alt="Screenshot 2025-10-02 233050" src="https://github.com/user-attachments/assets/383ebed1-d129-4bfb-8916-8acf0879dec0" />

**1. Click Add Firmware or press `A` / `Enter` on key board to add the `.bin` firmware in the `bin` folder.**

<img width="1220" height="506" alt="Screenshot 2025-10-02 233123" src="https://github.com/user-attachments/assets/0a410f1e-960d-4f8a-9d92-1f7904f7b2b7" />

**2. Browse your firmware file.**

<img width="756" height="370" alt="Screenshot 2025-10-02 233142" src="https://github.com/user-attachments/assets/d2515af3-14f4-4cf8-ae88-6f44462a25ba" />

**3. Connect your STM32 MCU to your PC via **ST-Link V2**.**

<img width="1302" height="716" alt="ST-LINK-V2" src="https://github.com/user-attachments/assets/eb7ceb87-1124-492f-abab-c1758185b13e" />


**4. (Optional) Check **Enable Firmware Protection** if you want to enable read protection (RDP1).**

<img width="806" height="416" alt="image" src="https://github.com/user-attachments/assets/d9580073-a57d-496c-89dc-b6577f6dba65" />

   
**5. Click **Install**.**

<img width="822" height="463" alt="image" src="https://github.com/user-attachments/assets/f62a9a72-1cfe-4e28-815c-67b5d8a25797" />
   
**The firmware will be flashed automatically with **real-time progress updates**.**

<img width="748" height="393" alt="image" src="https://github.com/user-attachments/assets/003a6774-80a8-4b45-bcdc-a46bd91d11b9" />


**You can also share this app along with your `.bin` file in the `bin` folder. It works like a **package installer**, allowing someone else to flash the MCU with **just one click**.**

---

## ⚙️ External Tools

This application does **not include or bundle** any STMicroelectronics software.  
It simply sends standard command-line instructions to **ST-LINK_CLI.exe** if it is already installed on your system.

`ST-LINK_CLI.exe` is a proprietary tool developed by **STMicroelectronics** for communicating with STM32 devices.  
You must install it separately using one of the following:
- **ST-LINK Utility**  
- **Arduino STM32 Core** STM32F1xx/GD32F1xx boards by stm32duino
- Usage of `ST-LINK_CLI.exe` is subject to **STMicroelectronics’ license terms**, independent of this software.

---

### ⚙️ Supported STM32 MCU Families

| Family | Core | Example Devices |
|:--------|:------|:----------------|
| **STM32F0** | Cortex-M0 | F030, F042, F072, F091 |
| **STM32F1** | Cortex-M3 | F100, F103, F105, F107 |
| **STM32F2** | Cortex-M3 | F205, F215, F207, F217 |
| **STM32F3** | Cortex-M4 | F301, F302, F303, F334, F373 |
| **STM32F4** | Cortex-M4 | F401, F405, F407, F411, F429, F446 |
| **STM32F7** | Cortex-M7 | F722, F746, F767, F769 |
| **STM32G0** | Cortex-M0+ | G030, G031, G041, G070, G071, G081 |
| **STM32G4** | Cortex-M4 | G431, G441, G474, G484 |
| **STM32L0** | Cortex-M0+ | L011, L031, L051, L071, L072, L081 |
| **STM32L1** | Cortex-M3 | L100, L151, L152, L162 |
| **STM32L4 / L4+** | Cortex-M4 | L412, L432, L452, L462, L476, L496, L4R5 |

---

## ⚠️ Important Notes
- The app **does not redistribute** or embed `ST-LINK_CLI.exe`.  
- It **interacts externally** with it (similar to running commands in Command Prompt).  
- Users must ensure compliance with **STMicroelectronics’ licensing terms**. 

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

## 🧩 Installation

1. Download the latest release from the [Releases](https://github.com/aneeshmurali-n/AMN-STM32-Flasher/releases) page.    
2. Run `AMN STM32 Flasher setup.exe`.  
3. Add your firmware and start flashing!

---

## 🔐 File Integrity Verification (SHA-256 Checksums)

> 🛡️ **Verify your download:**  
> These SHA-256 checksums let you confirm that your files are authentic and haven’t been modified.

| File | Description | SHA-256 |
|------|--------------|----------|
| `AMN STM32 Flasher.exe` | Core standalone application | `EE811486F52A878FF453BF650C968989F583C549C09B101FE776E99A0DED81B0` |
| `AMN STM32 Flasher Setup.exe` | Windows standalone application installer | `4C41FF92CB2E0F05768DC9E6B2E64F0C5876B05B436035D4BF39866D2DF16421` |

---

### 🧮 Verify the Hash

You can verify the file’s authenticity using **Windows PowerShell** (built into Windows 10 & 11).

1. Go to the folder where the files are saved.  
2. **Hold Shift + Right-click** inside the folder background and select **“Open PowerShell window here”** or **"Open in Terminal"**.  
3. Run the command for the file you want to check:
4. Compare the result with the SHA-256 hash listed above.<br>
   ✅ If they match — the file is safe.<br>
   ⚠️ If not — re-download it from the official releases page.<br>
   
```

Get-FileHash "AMN STM32 Flasher Setup.exe" -Algorithm SHA256

```

```

Get-FileHash "AMN STM32 Flasher.exe" -Algorithm SHA256

```


## Why Use This App?
- Converts firmware into an installer-style package.
- Simplifies STM32 firmware updates for beginners.
- Automates repetitive flashing for professionals.
- Makes STM32 projects easy to distribute and reproduce.
  
---

## Credits
- **Aneesh Murali Nariyampully** – Original Author & Developer  
- **CustomTkinter** – MIT License (by Tom Schimansky)  
- **Python Software Foundation** – Python 3.x Standard Library  
- **STMicroelectronics** – ST-LINK_CLI.exe (External Command-Line Tool)  
- **Inno Setup Compiler** – Freeware by Jordan Russell, used to create the Windows installer.
  
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

- This software is provided “as is”, without warranty of any kind, express or implied.  
- The developer is not responsible for any damage to hardware, firmware, or data that may result from use or misuse of this application.  
- Users should verify that they are flashing the correct firmware and using compatible devices.  
- `ST-LINK_CLI.exe` is the property of **STMicroelectronics** and must be used in accordance with their licensing terms.

---

## 🌐 Project Information
- **Author:** Aneesh Murali Nariyampully  
- **Repository:** [https://github.com/aneeshmurali-n/AMN-STM32-Flasher](https://github.com/aneeshmurali-n/AMN-STM32-Flasher)  
- **License:** [Apache 2.0](LICENSE)  
- **Notice:** [NOTICE.txt](NOTICE.txt)

---

Made with ❤️ by Aneesh Murali Nariyampully  
If this project helps you, please ⭐ it on GitHub!


  
