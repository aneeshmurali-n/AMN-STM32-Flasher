# AMN STM32 Flasher  
![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13%2B-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11-lightgrey.svg)
![UI](https://img.shields.io/badge/UI-Dark_Purple_Green_by_AMN-9cf.svg)
<img width="921" height="521" alt="Screenshot 2025-10-27 200448" src="https://github.com/user-attachments/assets/5094becb-86de-4500-a479-d2cc75438f26" />

## The world’s first flashing app that makes flashing as easy as moving a file.
No terminals. No setup. Just drop — and done.

Flashing STM32 firmware has never been this simple.  
**AMN STM32 Flasher** replaces command lines and scripts with a single action:  
**drag and drop** your `.bin` file — the app detects your ST-LINK, erases memory,  
installs, verifies, and protects your firmware automatically.

Built for developers, engineers, and makers who value **speed**, **clarity**, and **style**.  
Everything just works  beautifully.

---

## 🧭 Vision

> ### *“Flashing firmware should be as simple as moving a file.”*

AMN STM32 Flasher redefines how developers interact with embedded hardware.  
It’s fast, intuitive, and designed with the same care as the devices it programs.  
For the first time, flashing feels human.

---

## 🧠 What Makes It Different

Where others demand commands, AMN Flasher listens to intent.  
It detects your tools, flashes your board, and visualizes the process — automatically.  

Everything you touch in the app is alive:  
Every button adapts, every widget responds, every action has a shortcut.  

> It doesn’t just work — it understands what you want to do.

---


## 🖼️ Experience It Yourself

https://github.com/user-attachments/assets/d1410449-6070-4b46-9c99-8fda1862d6a8

> **AMN STM32 Flasher**  
> Flashing firmware is as simple as moving a file — and it’s never looked this good.



---


## 🚀 Key Features

| ✨ Feature | 💡 Description |
|------------|----------------|
| 🖱️ **Drop Flash** | Just drop your `.bin` file — AMN Flasher detects your ST-LINK, erases, flashes, protects, and verifies automatically. |
| ⚡ **Instant Flash Mode** | Flash the moment you drop. No buttons. No setup. Just flow. |
| 🧠 **Smart ST-LINK Detection** | Finds your ST-LINK CLI automatically and remembers it — no configuration, no effort, it just works. |
| 🔒 **Firmware Protection** | Lock your code with one click. Enable or disable STM32 Readout Protection instantly. |
| 🎚️ **Dynamic Action Buttons** | Buttons that think. Each adapts to your workflow — *Install* when ready, *Add Firmware* when clear. |
| 🎛️ **Live Flash Feedback** | Smooth 60 FPS animation visualizes every step — erase, program, verify, protect. |
| 🧩 **Single-Instance Engine** | Always one window. If it’s open, AMN Flasher simply focuses it — intelligently. |
| 🪟 **Native Windows Integration** | Built on real Win32 APIs for true drag-and-drop behavior and desktop fluidity. |
| 🎨 **Dark Purple Green Theme** | Designed by AMN for clarity, comfort, and focus — elegance in every pixel. |
| ⌨️ **Keyboard-First Workflow** | Every action has a shortcut. Flash, clear, protect — all from your fingertips. |
| 🧭 **Fully Interactive Interface** | Every widget responds. Every control reacts. Nothing is static. Everything feels alive. |


> **Every widget responds. Every action has a shortcut.**
> 
> AMN STM32 Flasher turns every interaction into a seamless experience.

 
---


## 🧰 Installation

### 🔹 Requirements
- 🪟 **Windows 10 / 11 (64-bit)**
- 🔗 [**ST-LINK Utility**](https://www.st.com/en/development-tools/stsw-link004.html)  
  *(Includes `ST-LINK_CLI` and ST-LINK drivers — provided by STMicroelectronics.)*  
  We recommend installing the **official ST-LINK Utility** for best performance.  
  If you’ve already installed STM32 board support in the **Arduino IDE**, that’s also sufficient.

### 🔹 Steps
1. Download the latest version from the [📦 Releases](https://github.com/aneeshmurali-n/AMN-STM32-Flasher/releases) page.  
2. Run **`AMN STM32 Flasher Setup.exe`** and complete the installation.  
3. Launch **AMN STM32 Flasher**.  


---


## 🧠 How to Use

1. **Connect** your STM32 board to your PC via ST-LINK. <br><img src="https://github.com/user-attachments/assets/a8f0b54b-7528-47a7-b5be-76b1df36f363"  width=100%><br>
2. **Open** AMN STM32 Flasher. <br> <img src="https://github.com/user-attachments/assets/d7261a38-64cb-4dfc-afab-36d5febc69d6" width=100%> <br>
3. **Drop or select** your `.bin` firmware file.  <br> <img src="https://github.com/user-attachments/assets/b305e860-ac6f-495f-872f-67739d9a49b6" width=100%>  <br>
4. **Click “Install”** — or do nothing if Instant Flash Mode is enabled.  <br> <img  src="https://github.com/user-attachments/assets/07a2c6a7-20e9-4119-864a-478bc3c8ca7f" width=100%>  <br>
5. **Done.** Your firmware is installed, verified, and optionally protected.  <br> <img src="https://github.com/user-attachments/assets/56165bdf-e8cd-4e22-ac78-3aec1aa1b57f" width=100%>  <br>

> ✨ Everything happens automatically — simply connect, drop, and flash.
> 
> ⚡ No terminal. No manual setup. Just a **file drop**


---


## ⌨️ Keyboard Shortcuts

| Shortcut       | Action                                      |
|----------------|---------------------------------------------|
| `Q`            | ⚡ Toggle Drop Flash Mode (Enable / Disable)|
| `D` / `Delete` | 🧽 Clear firmware from workspace.           |
| `I` / `Enter`  | ⬇️ Install firmware                         |
| `A` / `Enter`  | ➕ Add firmware file                        |
| `P` / `E`      | 🔒 Enable / Disable Read Protection (RDP1)|

> Every action is one keystroke away.


---


## ⚙️ Configuration

The configuration file is automatically created at:  
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

`FLASH_START_ADDR` — Start address for firmware flashing (default 0x08000000, standard for most STM32 MCUs).
Only change this if you are flashing to a custom memory region.

`DROP_FLASH` — Controls Instant Flash Mode (`ENABLED` / `DISABLED`)

> The app manages this file automatically — manual edits are rarely needed.


---


### ✅ Compatibility

Supports all STM32 microcontrollers compatible with ST-LINK CLI over SWD.  
Default flash region: `0x08000000`.  
Advanced users can adjust this address in the configuration file.


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
- 🎨 **CustomTkinter** — for a clean and modern dark-themed UI 
- 🪟 **Win32 API (ctypes)** — native integration for real Windows drag-and-drop support  
- 💫 **Thread-Safe Architecture** — smooth, real-time feedback    
- ⚙️ **ST-LINK CLI**  — official STM32 programming tool (not bundled) 
  > 📎 *AMN STM32 Flasher does not include, modify, or distribute any STMicroelectronics software.*


---


## ⚠️ Important Notes

- **AMN STM32 Flasher** does not include or distribute `ST-LINK_CLI.exe` or any STMicroelectronics software.  
- The app communicates **securely and externally** with `ST-LINK_CLI.exe`, performing standard flash operations without modification.  
- Please install the **official STMicroelectronics ST-LINK Utility** to ensure compatibility and proper licensing.  
- For best results, keep the ST-LINK Utility in its default installation directory.  
- 💡 **No worries:** AMN STM32 Flasher automatically detects your ST-LINK path — no manual setup required.


---


## 🙌 Credits

- **Aneesh Murali Nariyampully** — Multidisciplinary Engineer, Creator, and Innovator  
  *Bridging Electronics, Embedded Systems, Software, and AI — all under one vision.*  
  *Original Author & Developer*  

- **CustomTkinter** — Modern UI framework for Python  
  Licensed under the **MIT License** by *Tom Schimansky.*

- **Python Software Foundation** — Developer of the **Python 3.x Standard Library.** 

- **STMicroelectronics** — Creator of **ST-LINK_CLI.exe**  
*(Official external command-line utility used by AMN STM32 Flasher. Not bundled, modified, or redistributed.)*

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


## The Philosophy

> “Flashing firmware should feel effortless.”  
> AMN STM32 Flasher turns a technical task into a natural gesture.  

Drag. Drop. Flash.  
The future of firmware programming starts here.


---


Made with ❤️ and precision by **Aneesh Murali Nariyampully**  
If this project inspired you or made your workflow easier, please ⭐ it on GitHub.



  
