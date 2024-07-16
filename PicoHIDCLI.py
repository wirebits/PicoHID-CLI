# PicoHID CLI
# A CLI tool that generates CircuitPython HID scripts from mnemonics for Raspberry Pi Pico Series.
# Author - WireBits

import os
import argparse

hidKeys = {
    'A': 'Keycode.A', 'B': 'Keycode.B', 'C': 'Keycode.C', 'D': 'Keycode.D', 'E': 'Keycode.E',
    'F': 'Keycode.F', 'G': 'Keycode.G', 'H': 'Keycode.H', 'I': 'Keycode.I', 'J': 'Keycode.J',
    'K': 'Keycode.K', 'L': 'Keycode.L', 'M': 'Keycode.M', 'N': 'Keycode.N', 'O': 'Keycode.O',
    'P': 'Keycode.P', 'Q': 'Keycode.Q', 'R': 'Keycode.R', 'S': 'Keycode.S', 'T': 'Keycode.T',
    'U': 'Keycode.U', 'V': 'Keycode.V', 'W': 'Keycode.W', 'X': 'Keycode.X', 'Y': 'Keycode.Y',
    'Z': 'Keycode.Z', 'F1': 'Keycode.F1', 'F2': 'Keycode.F2', 'F3': 'Keycode.F3', 'F4': 'Keycode.F4',
    'F5': 'Keycode.F5', 'F6': 'Keycode.F6', 'F7': 'Keycode.F7', 'F8': 'Keycode.F8', 'F9': 'Keycode.F9',
    'F10': 'Keycode.F10', 'F11': 'Keycode.F11', 'F12': 'Keycode.F12', 'LEFT': 'Keycode.LEFT_ARROW',
    'UP': 'Keycode.UP_ARROW', 'RIGHT': 'Keycode.RIGHT_ARROW', 'DOWN': 'Keycode.DOWN_ARROW',
    'TAB': 'Keycode.TAB', 'HOME': 'Keycode.HOME', 'END': 'Keycode.END', 'PGUP': 'Keycode.PAGE_UP',
    'PGDN': 'Keycode.PAGE_DOWN', 'CAPS': 'Keycode.CAPS_LOCK', 'NUM': 'Keycode.KEYPAD_NUMLOCK',
    'SCROLL': 'Keycode.SCROLL_LOCK', 'CTRL': 'Keycode.CONTROL', 'SHIFT': 'Keycode.SHIFT', 'ALT': 'Keycode.ALT',
    'GUI': 'Keycode.GUI', 'ESC': 'Keycode.ESCAPE', 'PRTSCR': 'Keycode.PRINT_SCREEN', 'PAUSE': 'Keycode.PAUSE',
    'SPACE': 'Keycode.SPACE', 'DEL': 'Keycode.DELETE', 'INSERT': 'Keycode.INSERT', 'BKSP': 'Keycode.BACKSPACE',
    'ENTER': 'Keycode.ENTER', 'APP': 'Keycode.APPLICATION'
}

class PicoHIDKeyboard:
    @staticmethod
    def convert_to_pico_script(pico_mnemonic):
        if pico_mnemonic.startswith("HID"):
            return "import time\nimport usb_hid"
        elif pico_mnemonic.startswith("HWD"):
            return "import board\nimport digitalio"
        elif pico_mnemonic.startswith("HLIB"):
            hid_lib = "from adafruit_hid.keycode import Keycode\n"
            hid_lib += "from adafruit_hid.keyboard import Keyboard\n"
            hid_lib += "from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS"
            return hid_lib
        elif pico_mnemonic.startswith("KYBD"):
            return "kbd = Keyboard(usb_hid.devices)\nlayout = KeyboardLayoutUS(kbd)"
        elif pico_mnemonic.startswith("PIN"):
            led_code = f"led = digitalio.DigitalInOut(board.GP25)\nled.direction = digitalio.Direction.OUTPUT"
            return led_code
        elif pico_mnemonic.startswith("LED"):
            led_value = (pico_mnemonic.split(" ")[1])
            if led_value == "ON":
                return "led.value = 1"
            elif led_value == "OFF":
                return "led.value = 0"
        elif pico_mnemonic.startswith("WAIT"):
            delay_time = int(pico_mnemonic.split(" ")[1])
            return f"time.sleep({delay_time / 1000})"
        elif pico_mnemonic.startswith("TYPE"):
            string_text = pico_mnemonic.split(" ", 1)[1]
            return f"layout.write(\"{string_text}\")"
        elif pico_mnemonic.startswith("SCODE"):
            keys = pico_mnemonic.split()[1:]
            key_sequence = [hidKeys[key] for key in keys]
            formatted_sequence = ', '.join(key_sequence)
            output_string = f"kbd.send({formatted_sequence})"
            return output_string
        elif pico_mnemonic.startswith("PCODE"):
            keys = pico_mnemonic.split()[1:]
            key_sequence = [hidKeys[key] for key in keys]
            formatted_sequence = ', '.join(key_sequence)
            output_string = f"kbd.press({formatted_sequence})\nkbd.release_all()"
            return output_string
        else:
            return pico_mnemonic

class PicoHIDMouse:
    @staticmethod
    def convert_to_pico_script(pico_mnemonic):
        if pico_mnemonic.startswith("MOUSE"):
            return "from adafruit_hid.mouse import Mouse"
        elif pico_mnemonic.startswith("MSE"):
            return "mse = Mouse(usb_hid.devices)"
        elif pico_mnemonic.startswith("MOVE"):
            try:
                _, x, y, w = pico_mnemonic.split()
                x = int(x)
                y = int(y)
                w = int(w)
                return f"mse.move({x}, {y}, {w})"
            except ValueError:
                return "Invalid parameters for MOVE command!"
        elif pico_mnemonic.startswith("CLICK"):
            cvalue = pico_mnemonic.split(" ", 1)[1]
            if cvalue == "LEFT":
                return "mse.click(Mouse.LEFT_BUTTON)"
            elif cvalue == "MIDDLE":
                return "mse.click(Mouse.MIDDLE_BUTTON)"
            elif cvalue == "RIGHT":
                return "mse.click(Mouse.RIGHT_BUTTON)"
        elif pico_mnemonic.startswith("PRESS"):
            pvalue = pico_mnemonic.split(" ", 1)[1]
            if pvalue == "LEFT":
                return "mse.press(Mouse.LEFT_BUTTON)\nmse.release_all()"
            elif pvalue == "MIDDLE":
                return "mse.press(Mouse.MIDDLE_BUTTON)\nmse.release_all()"
            elif pvalue == "RIGHT":
                return "mse.press(Mouse.RIGHT_BUTTON)\nmse.release_all()"
        else:
            return pico_mnemonic

def convert_text(duckpy_script):
    mnemonics = ""
    for line in duckpy_script.splitlines():
        converted_line = PicoHIDKeyboard.convert_to_pico_script(line.strip())
        if converted_line == line.strip():
            converted_line = PicoHIDMouse.convert_to_pico_script(line.strip())
        mnemonics += converted_line + '\n'
    return mnemonics

def main():
    parser = argparse.ArgumentParser(description="PicoHID CLI")
    parser.add_argument('-i', '--input', type=str, help="Input .txt file containing mnemonics", required=True)
    parser.add_argument('-c', '--convert', action='store_true', help="Convert mnemonics to Pico script", required=True)
    parser.add_argument('-s', '--save', action='store_true', help="Save the converted Pico script as code.py")
    parser.add_argument('-ps', '--saveas', type=str, help="Save the converted Pico script with a custom name, adding .py at the end")

    args = parser.parse_args()

    if args.input and not args.input.endswith('.txt'):
        print("Error: Input file must be a .txt file!")
        return

    if args.convert:
        try:
            with open(args.input, 'r') as file:
                duckpy_script = file.read()
                pico_script = convert_text(duckpy_script)
                
                if args.save:
                    output_file = 'code.py'
                    with open(output_file, 'w') as file:
                        file.write(pico_script)
                    print(f"Pico script saved to {output_file}.")
                elif args.saveas:
                    output_file = args.saveas
                    if not output_file.endswith('.py'):
                        output_file += '.py'
                    with open(output_file, 'w') as file:
                        file.write(pico_script)
                    print(f"Pico script saved to {output_file}.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()