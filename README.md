# PicoHID-CLI
A CLI tool that generates CircuitPython HID scripts from mnemonics for Raspberry Pi Pico Series.

# Key Features
- It takes `.txt` file for input mnemonics.
- It convert and save into CircuitPython HID Scripts in a single click.
- It save `.py` files in two ways :
  1. `code.py` file.
  2. With custom file name.

# OS Support
- Windows 10
- Windows 11
- Kali Linux

# Credits
The mnemoics used in this tool is heavily inspired by [Hak5](https://github.com/hak5) Ducky Script.

# Setup
Make sure that latest python and pip3 is installed on your system (Windows/Linux/MacOS).

# Installation and Setup of Circuit Python
1. Download Circuit Python `.uf2` file :
   - Raspberry Pi Pico - [here](https://circuitpython.org/board/raspberry_pi_pico/)
   - Raspberry P i Pico W - [here](https://circuitpython.org/board/raspberry_pi_pico_w/)
   - Latest version is `9.1.0` for both.
2. Connect Raspberry Pi Pico or Pico W with a USB cable.
3. Press and hold the `BOOTSEL` button and connect to the PC/Laptop.
   - When it connects, then Raspberry Pi Pico or Pico W show as a removable storage device named `RPI-RP2`.
   - When `RPI-RP2` is showing, then release the bootsel button.
4. Copy the `uf2` file in the `RPI-RP2`.
   - When it is copied, then it disconnects automatically and reconnect as `CIRCUITPY`.
   - Means circuit python is successfully flashed in the Raspberry Pi Pico or Pico W.
5. Open `CIRCUITPY`.
   - There are two important things in it : `lib` folder and `code.py` file.
6. Download Adafruit CircuitPython Bundle from [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
   - Latest is `adafruit-circuitpython-bundle-9.x-mpy-20240709.zip`.
7. Extarct the ZIP file.
8. Go to the `lib` folder in the extracted ZIP file.
9. Copy `adafruit_hid` folder in the `lib` folder of `CIRCUITPY`.
10. Done! Now, Raspberry Pi Pico or Pico W is ready to use as a USB Rubber Ducky.

# Parameters
There are 4 parameters :
1. *-i* - Input Mnemonic Text File.
2. *-c* - Convert the mnemonics into circuitpython HID script.
3. *-s* - Default save with file name `code.py`.
4. *-p* - Save with custom name.

# Supported Boards
- Raspberry Pi Pico
- Raspberry Pi Pico W
- Waveshare RP2040 Zero

# Mnemonic Table
| Mnemonics | Description | Example  |
|-----------|-------------|----------|
| TIME       | It adds the time library in the code.     | Just type TIME     |
| HWD       | It adds the board and digitalio libraries in the code.  | Just type HWD     |
| HID      | It adds the usb_hid, Keycode, Keyboard and KeyboardLayoutUS libraries in the code.| Just type HID|
| MOUSE     | It adds the Mouse library in the code.| Just type MOUSE|
| KYBD		| It create objects for keycode and keyboard layout in the code.| Just type KYBD|
| MSE       | It create objects for mouse in the code.| Just type MSE|
| PIN       | It add pin declaration in the code.| Just type PIN|
| LED       | It turns on/off the led in the code.<br>Values are ON and OFF.| LED ON|
| WAIT      | It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second.| WAIT 1000|
| TYPE      | It add text want to type in the code.| TYPE Hello World!|
| MOVE      | It moves the mouse pointer according to the values.<br>Values are x-axis, y-axis and scroll.<br> Values may be positive, negative or ZERO.<br>Values in sequence - x-axis, y-axis, scroll.| MOVE 36 -78 0|
| CLICK     | It clicks the mouse buttons.<br>Values are LEFT, MIDDLE and RIGHT.| CLICK LEFT|
| PRESS     | It press the mouse buttons and relaese immediately.<br>Values are LEFT, MIDDLE and RIGHT.| PRESS RIGHT|

The above mnemonic table is in pdf now.

# Supported Mnemonics
## Alphabet Keys
`A` `B` `C` `D` `E` `F` `G` `H` `I` `J` `K` `L` `M` `N` `O` 
`P` `Q` `R` `S` `T` `U` `V` `W` `X` `Y` `Z`
## Function Keys
`F1` `F2` `F3` `F4` `F5` `F6` `F7` `F8` `F9` `F10` `F11` `F12`
## Navigation Keys
`LEFT` `UP` `RIGHT` `DOWN` `TAB` `HOME` `END` `PGUP` `PGDN`
## Lock Keys
`CAPS` `NUM` `SCROLL`
## System and GUI Keys
`GUI` `ESC` `PRTSCR` `PAUSE`
## Editing Keys
`INSERT` `DEL` `BKSP` `ENTER`
## Modifier Keys
`CTRL` `SHIFT` `ALT`

# Before...
Write down your mnemonics and save in it `.txt` file.

# Install and Run
1. Download or Clone the Repository.
2. Open the folder and click on address bar.
3. Type `cmd` or `powershell`.

## Default Save

```
python PicoHIDCLI.py -i notepad.txt -c -s
```
## Save with custom name

```
python PicoHIDCLI.py -i notepad.txt -c -p note
```
4. Paste the code in the `code.py` file in the `CIRCUITPY`.
   - It ask for replacing, then click on `Yes`.
   - Be Careful! As it is saved the script start executing.

# Start/Stop the Raspberry Pi Pico or Pico W
1. If want to stop Raspberry Pi Pico or Pico W from execution, then connect the Male-To-Male jumper wires as shown in image below : 

![RPIPICO](https://github.com/wirebits/PicoHID-Scripter/assets/159493381/1be784c2-cc24-48e0-baa8-d3b94bc7646e)

![RPIPICOW](https://github.com/user-attachments/assets/f650002d-c8a8-4795-bbbd-b6a929dc5af9)

2. If want to start again the execution, simply remove the jumper wires.

# Examples
## 1. Open Notepad and Type
Mnemonic for Open Notepad and Type

```
TIME
HID

KYBD

GUI R
WAIT 1000
TYPE notepad
WAIT 1000
ENTER
WAIT 1000
TYPE This is a test for Raspberry Pi Pico script developed by PicoHID CLI!
```
after Convert, the circuit python script of the following mnemonic is :

```
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

kbd.press(Keycode.GUI, Keycode.R)
kbd.release_all()
time.sleep(1.0)
layout.write("notepad")
time.sleep(1.0)
kbd.send(Keycode.ENTER)
time.sleep(1.0)
layout.write("This is a test for Raspberry Pi Pico script developed by PicoHID Scripter!")
```
Just copy this code and paste it in the `code.py` file in the `CIRCUITPY`.

## 2. Open CMD as Administartor Mode
Mnemonic for Open CMD as Administartor Mode

```
TIME
HID

KYBD

GUI
WAIT 1000
TYPE cmd
WAIT 1000
CTRL SHIFT ENTER
WAIT 1200
ALT Y
```
after Convert, the circuit python script of the following mnemonic is :

```
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

kbd.send(Keycode.GUI)
time.sleep(1.0)
layout.write("cmd")
time.sleep(1.0)
kbd.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER)
kbd.release_all()
time.sleep(1.2)
kbd.press(Keycode.ALT, Keycode.Y)
kbd.release_all()
```
Just copy this code and paste it in the `code.py` file in the `CIRCUITPY`.

## 3. Create a folder
Mnemonic for Create a folder

```
TIME
HID

KYBD

CTRL SHIFT N
WAIT 1200
ENTER
```
after Convert, the circuit python script of the following mnemonic is :

```
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

kbd.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.N)
kbd.release_all()
time.sleep(1.2)
kbd.send(Keycode.ENTER)
```
Just copy this code and paste it in the `code.py` file in the `CIRCUITPY`.
