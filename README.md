# Bucket's Hackpad: RP2040 Macro Keyboard ⌨️

A custom, open-source 6-key macropad project utilizing the Seeed XIAO RP2040 microcontroller for USB input and RGB lighting.

---

## ✨ Features
*   **Microcontroller:** Seeed XIAO RP2040 (motherboard of the keyboard)
*   **Switches:** MX-Style switches (6 keys total)
*   **Lighting:** SK6812 MINI-E LEDs (RGB lighting for the keyboard)
*   **Design Tools:** Schematic & PCB designed using **KiCad**; Case designed using **Autodesk Fusion**

## 🛠️ Bill of Materials (BOM)
| Item | Quantity | Description |
| :--- | :---: | :--- |
| Seeed XIAO RP2040 | x1 | Main motherboard |
| MX-Style switches | x6 | The keys of the keyboard |
| SK6812 MINI-E LEDs | x2 | RGB lighting |
| M3x16mm screws | x4 | For joining the top and bottom of the case |
| 3D Printed Case | x1 | Custom enclosure |

| case.png | PCB.png | Schematic.png |
| :---: | :---: | :---: |
| ![images/case.png](Case Enclosure) | ![images/PCB.png](PCB Layout) | ![images/Schematic.png](Circuit Schematic) |
;


## 📁 Project Structure
The design files are organized as follows:

### KiCad Files
Found in the main directory (or a `pcb/` folder if you organize it that way):
*   `[your-project-name].kicad_pro`: The main project file
*   `[your-project-name].kicad_sch`: The schematic file
*   `[your-project-name].kicad_pcb`: The PCB layout file

### Fusion 360 Files
The 3D model for the top and bottom case components can be found here. The enclosure was designed with an education license for 3D printing.

*   `[Case Top File]`: (e.g., `case-top.f3d` or `.step`)
*   `[Case Bottom File]`: (e.g., `case-bottom.f3d` or `.step`)

## 💡 How It Was Made
The project was created by wiring the switches in a matrix and routing the PCB in KiCad. The mechanical enclosure design took significant effort to finalize the exact dimensions in Fusion 360.

## 😄 Acknowledgments & Motivation
*   Quote inspiration: "Dream, dream, dream. Dreams transform into thoughts and thoughts result in action." - Dr. A.P.J. Abdul Kalam
*   A classic joke to lighten the mood: Why don't skeletons fight each other? Because they don't have the guts. LOL!

## 📜 License
*Add your license information here, e.g., MIT License.*
# Bucket-s-hackpad
