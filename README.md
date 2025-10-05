# AMN STM32 Flasher  
![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12%2B-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows_10/11-lightgrey.svg)
![UI](https://img.shields.io/badge/UI_Dark_purple_green_by_AMN-CustomTkinter-9cf.svg)

**AMN STM32 Flasher** is a one-click **firmware flasher** and **installable firmware package creator** for STM32 microcontrollers.  
It makes flashing STM32 devices **as easy as installing a regular application**.  

<img width="1920" height="1080" alt="exp_1 1 1" src="https://github.com/user-attachments/assets/6970617b-b619-4b57-960d-ee9d183b4b93" />


<br>
<br>
You can use it in two ways:

### 🧩 Option 1 – As a Firmware Package Creator
Simply click **Add Firmware**, then press **C** to create an installable firmware package.  
Share the generated package — and your users can:

1. **Extract** the firmware package.  
2. **Connect** their STM32 MCU to a PC via an **ST-Link programmer**.  
3. **Run** the `AMN STM32 Flasher.exe` file inside the extracted folder.  
4. *(Optional)* Enable **Firmware Protection (RDP1)** if desired, then click **Install**.  

The firmware will be automatically written to the chip —  
no source code, no IDE, and no complex setup required.  

### ⚡ Option 2 – As a Flashing Tool
You can also use **AMN STM32 Flasher** directly as a standard flasher.  
Just install it like a regular application, then:

1. **Run the app** from the desktop shortcut.  
2. Press **A** or **Enter** (or click **Add Firmware**) to select your `.bin` firmware.  
3. *(Optional)* Enable **Firmware Protection** if you want to activate read protection.  
4. Press **Enter** or click **Install** to flash your STM32 device instantly.  

This tool is perfect for **beginners and non-experienced users**, allowing anyone to try STM32 projects **without compiling code or setting up development environments**.  
It also **saves time for experienced embedded engineers** through fully automated flashing and package creation.

---

## ✨ Features
- **Easy Firmware Flashing** – Install firmware as easily as a standard application.  
- **One-Click Flash** – Flash your device with a single click.  
- **Create Firmware Installer** – Package your firmware as a single-click installer.  
- **Automatic Firmware Detection** – Detects `.bin` firmware files in the `bin` folder automatically.  
- **ST-LINK_CLI Command Integration** – Sends commands to `ST-LINK_CLI.exe` if installed.  
- **Modern Dark UI** – Sleek dark mode interface with a purple-green theme.  
- **Optional Firmware Protection** – Enable/disable read protection (RDP1).  
- **Smooth Progress Feedback** – Real-time progress bar and status updates.  
- **Keyboard Shortcuts** – Quickly access key functions without using the mouse.  

---

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

## ⚙️ External Tools

This application does **not include or bundle** any STMicroelectronics software.  
It simply sends standard command-line instructions to **ST-LINK_CLI.exe** if it is already installed on your system.

`ST-LINK_CLI.exe` is a proprietary tool developed by **STMicroelectronics** for communicating with STM32 devices.  
You must install it separately using one of the following:
- **ST-LINK Utility**  
- **STM32CubeProgrammer**  
- **Arduino STM32 Core** (STM32F1xx / GD32F1xx boards)

Usage of `ST-LINK_CLI.exe` is subject to **STMicroelectronics’ license terms**, independent of this software.

---

### ⚙️ Supported STM32 MCU Families

| Family | Core | Example Devices | Notes |
|:--------|:------|:----------------|:--------|
| **STM32F0** | Cortex-M0 | F030, F042, F072, F091 | Entry-level series, fully supported |
| **STM32F1** | Cortex-M3 | F100, F103, F105, F107 | Classic and widely used family |
| **STM32F2** | Cortex-M3 | F205, F215, F207, F217 | Works identically to F4 series |
| **STM32F3** | Cortex-M4 | F301, F302, F303, F334, F373 | Mixed-signal line, fully supported |
| **STM32F4** | Cortex-M4 | F401, F405, F407, F411, F429, F446 | Verified and stable operation |
| **STM32F7** | Cortex-M7 | F722, F746, F767, F769 | Fully supported; same memory base |
| **STM32G0** | Cortex-M0+ | G030, G031, G041, G070, G071, G081 | Low-cost series, no special handling needed |
| **STM32G4** | Cortex-M4 | G431, G441, G474, G484 | Fully supported |
| **STM32L0** | Cortex-M0+ | L011, L031, L051, L071, L072, L081 | Ultra-low-power line, stable support |
| **STM32L1** | Cortex-M3 | L100, L151, L152, L162 | Fully compatible with RDP and mass erase |
| **STM32L4 / L4+** | Cortex-M4 | L412, L432, L452, L462, L476, L496, L4R5 | Fully supported; verified with ST-LINK CLI |

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

## Why Use This App?
- Converts firmware into an installer-style package.
- Simplifies STM32 firmware updates for beginners.
- Automates repetitive flashing for professionals.
- Makes STM32 projects easy to distribute and reproduce.
  
---

## Credits
- Aneesh Murali Nariyampully – Original author & developer  
- CustomTkinter – MIT License (by Tom Schimansky)  
- Python Software Foundation – Python 3.x Standard Library
- STMicroelectronics – ST-LINK_CLI.exe (external command-line tool)

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
- **Notices:** [NOTICE](NOTICE.txt)

  
