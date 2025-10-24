# AMN STM32 Flasher  
![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13%2B-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11-lightgrey.svg)
![UI](https://img.shields.io/badge/UI-Dark_Purple_Green_by_AMN-9cf.svg)

## 🏆 The World’s First Drag-and-Drop Firmware Flasher

**No terminals. No setup. No stress.**  
Just **drop your firmware** — and watch your STM32 flash itself.

Flashing STM32 firmware has never been this simple.  
**AMN STM32 Flasher** replaces command lines and scripts with a single action:  
**drag and drop** your `.bin` file — the app detects your ST-LINK, erases memory,  
installs, verifies, and protects your firmware automatically.

Built for developers, engineers, and makers who value **speed**, **clarity**, and **style**.  
Everything just works  beautifully.

---

## 🧭 Vision

> ### *“Flashing firmware should be as simple as moving a file.”*

**AMN STM32 Flasher** isn’t just another tool — it’s a statement.  
It redefines how developers interact with embedded hardware:  
simple, fast, and beautifully intuitive.

For the first time, flashing firmware feels **human.**

---






## 🖼️ Experience It Yourself
> **AMN STM32 Flasher**  
> Flashing firmware is as simple as moving a file — and it’s never looked this good.

https://github.com/user-attachments/assets/b04cfcef-0064-489c-aa19-83244bffc553

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

| Shortcut       | Action                                      |
|----------------|---------------------------------------------|
| `Q`            | ⚡ Toggle Drop Flash Mode (Enable / Disable)|
| `D` / `Delete` | 🧽 Clear firmware from workspace.           |
| `I` / `Enter`  | ⬇️ Install firmware                         |
| `A` / `Enter`  | ➕ Add firmware file                        |
| `P` / `E`      | 🔒 Enable / Disable Read Protection (RDP1)|


---

## 🧠 Why It’s Different

**AMN STM32 Flasher** was built for humans.

It’s the first tool that turns flashing into a **single natural action** — just drop your `.bin` file.  
No setup, no scripts, no console output — everything happens automatically.  

It detects your ST-LINK, erases, flashes, verifies, and protects your firmware —  
with live progress, instant feedback, and a clean, modern interface.  

> ⚡ **Where others demand commands, AMN STM32 Flasher just works.**

---


## 🧰 Installation

### 🔹 Requirements
- 🪟 **Windows 10 / 11 (64-bit)**
- 🐍 **Python 3.13+** *(only required for development or source builds)*
- 🔗 [**ST-LINK CLI**](https://www.st.com/en/development-tools/stsw-link004.html)  
  *(Included in the official ST-LINK Utility package from STMicroelectronics)*

### 🔹 Steps
1. Download the latest version from the [📦 Releases](https://github.com/aneeshmurali-n/AMN-STM32-Flasher/releases) page.  
2. Run **`AMN STM32 Flasher Setup.exe`** and complete the installation.  
3. Launch the app.  
4. Drag and drop your `.bin` firmware file — flashing begins automatically!  

> ⚡ No terminal. No manual setup. Just **drop and flash.**

---


## ⚠️ Important Notes

- **AMN STM32 Flasher** does not include or distribute `ST-LINK_CLI.exe` or any STMicroelectronics software.  
- The application only **communicates externally** with `ST-LINK_CLI.exe`, executing standard command-line operations securely and transparently.  
- Users must install the official **ST-LINK Utility** separately and ensure compliance with **STMicroelectronics’ licensing terms**.  
- For best results, keep the ST-LINK Utility installed in its default directory
- 💡 **No worries:** AMN STM32 Flasher automatically detects the correct ST-LINK path — no manual setup required.


---

## 💡 How It Works

1. **Launch** the app  
2. **Drop or Select** your `.bin` firmware  
3. **Click “Install”** or Do nothing — if Drop Flash is enabled, it starts instantly.  
4. **Done.**  
   Your firmware is installed, verified, and optionally protected.

<p align="center">
  <img src="assets/screen_ready.png" width="30%">
  <img src="assets/screen_flash.png" width="30%">
  <img src="assets/screen_protected.png" width="30%">
</p>

---

### ✅ Supported STM32 MCU Families

**AMN STM32 Flasher** supports all STM32 microcontrollers compatible with **ST-LINK CLI** over **SWD (Serial Wire Debug)**.  
By default, it operates at memory address **0x08000000** — the standard flash region for STM32 devices.  
  
Advanced users can easily change the **flash start address** in the configuration file  
(`Documents/AMNSTM32Flasher/settings.json`) to match custom memory layouts or bootloader offsets.


---



## ⚙️ Configuration File (`settings.json`)

The configuration file is automatically created in:  
`Documents/AMNSTM32Flasher/settings.json`

You can edit this file to adjust flashing behavior and preferences.

### 🧩 Example:
```json
{
    "FLASH_START_ADDR": "0x08000000",
    "DROP_FLASH": "ENABLED"
}
```
💡 Parameters

FLASH_START_ADDR — Defines the starting memory address for firmware flashing.
Default: 0x08000000 (standard for most STM32 MCUs).
Only change this if you are flashing to a custom memory region.

DROP_FLASH — Stores the current state of the Drop Flash feature.

"ENABLED" → Automatically flashes when a .bin file is dropped into the window.

"DISABLED" → File drop still replaces the previous firmware, but flashing occurs only when you press Install or use shortcuts.

⚙️ The app manages this file automatically — manual edits are optional and rarely needed.

---

## 🧩 Architecture Overview

| Module | Purpose |
|--------|----------|
| `AMN_STM32_Flasher_v1.0.0.0.py` | Core GUI + Flashing logic |
| `amn_instance.py` | Single-instance mutex controller |
| `amn_drop.py` | Native Windows drag-in handler |
| `amn_dragout.py` | Detects drag-out gestures |
| `amn_drag_simulator.py` | Floating drag text animation |
| `pathfinder.py` | ST-LINK CLI auto-detection |
| `formatter.py` | Human-readable firmware naming |
| `theme.py` | Custom dark theme |

---

## 🧬 Built With

- 🐍 **Python 3.13+** — lightweight, powerful, and portable foundation  
- 🎨 **CustomTkinter** — for a clean, modern, dark-themed user interface  
- 🪟 **Win32 API (ctypes)** — native integration for real Windows drag-and-drop support  
- 💫 **Thread-Safe Architecture** — smooth, non-blocking progress updates and real-time feedback  
- ⚙️ **ST-LINK CLI** *(external dependency, not bundled)* — official STM32 programming tool used **only if installed** on the system  
  > 📎 *AMN STM32 Flasher does not include, modify, or distribute any STMicroelectronics software.*

---

## 🙌 Credits

- **Aneesh Murali Nariyampully** — Multidisciplinary Engineer, Creator, and Innovator  
  *Bridging Electronics, Embedded Systems, Software, and AI — all under one vision.*  
  *Original Author & Developer*  

- **CustomTkinter** — Modern UI framework for Python  
  Licensed under the **MIT License**, by *Tom Schimansky*  

- **Python Software Foundation** — Python 3.x Standard Library  

- **STMicroelectronics** — Developer of **ST-LINK_CLI.exe**  
  *(External command-line utility used by AMN STM32 Flasher; not bundled or modified.)*  

- **Inno Setup Compiler** — Freeware by *Jordan Russell*, used to create the Windows installer.

  
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

## ⚠️ Disclaimer

- This software is provided **“as is”**, without any warranty of any kind — express or implied.  
- The developer assumes **no responsibility or liability** for any damage to hardware, firmware, or data resulting from the use or misuse of this application.  
- Users are responsible for ensuring that they flash the **correct firmware** and use **compatible STM32 devices**.  
- **`ST-LINK_CLI.exe`** is the property of **STMicroelectronics** and must be used in full compliance with their respective **software licensing terms**.


---

## 🌐 Project Information

- **Author:** **Aneesh Murali Nariyampully** — Multidisciplinary Engineer, Creator, and Innovator  
  *Bridging Electronics, Embedded Systems, Software, and AI — all under one vision.*  
  *Original Author & Developer*  

- **Repository:** [github.com/aneeshmurali-n/AMN-STM32-Flasher](https://github.com/aneeshmurali-n/AMN-STM32-Flasher)  
- **License:** [Apache License 2.0](LICENSE)  
- **Notice:** [NOTICE.txt](NOTICE.txt)

---

## ⭐ Support the Project

If you believe in creating **simple tools that empower everyone**,  
please consider giving this project a **⭐ star on GitHub** —  
it helps others discover and support this innovation.

> **AMN STM32 Flasher** — makes flashing as simple as moving a file.*  
> *Drag. Drop. Flash.*  
> The future of firmware programming starts here.

---

Made with ❤️ and precision by **Aneesh Murali Nariyampully**  
If this project inspired you or made your workflow easier, please ⭐ it on GitHub.



  
