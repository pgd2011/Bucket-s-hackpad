import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import (
    KC,
    Keycode,
)
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.hid import HIDModes
import adafruit_hid.consumer_control_code as consumer

keyboard = KMKKeyboard()
keyboard.hid_mode = HIDModes.USB

# --- Module Setup ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
rgb_ext = RGB()
keyboard.modules.append(rgb_ext)

# --- Pin Mapping and Matrix Setup ---

# Define the pins based on your schematic (assuming Col 4 moves to GP6)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.col_pins = (board.GP3, board.GP4, board.GP7, board.GP6) # Assuming GP1 (Col 4) moved to GP6

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Configure the rotary encoder pins and behavior
# A pin (GP0), B pin (GP1), Switch pin (GP10 - which is Col 1, Row 4 intersection)
encoder_handler.pins = (
    (board.GP0, board.GP1, board.GP10, False), # (A, B, Switch pin, is_inverted)
)

# Map encoder rotation to Volume Up/Down
encoder_handler.map = [
    ((consumer.VOLUME_INCREMENT,), (consumer.VOLUME_DECREMENT,), None,), # Layer 0: CW, CCW, Switch
]

# --- Keymap Definition ---

# Define a function to toggle RGB lighting
TOGGLE_RGB = KC.RGB_TOG

# Map the standard keys (4x4 matrix plus the encoder button)
keyboard.keymap = [
    [
        # ROW 1            ROW 2            ROW 3            ROW 4
        # Col 1   Col 2   Col 3   Col 4    (Using a tuple for keycodes)
        KC.FSLASH, KC.ASTERISK, KC.MINUS, KC.PLUS,
        KC.N1,     KC.N2,     KC.N3,     KC.N4,
        KC.N5,     KC.N6,     KC.N7,     KC.N8,
        KC.N9,     KC.DOT,    **KC.ENTER**,     KC.NO, # ENTER added here
    ]
]

# Map the encoder switch press action in the encoder handler module
# The switch is connected to GP10 (Row 4, Col 1 connection in matrix logic)
# This will be mapped to the TOGGLE_RGB action
keyboard.macro_map = {
    KC.RGB_TOG: TOGGLE_RGB
}

if __name__ == '__main__':
    keyboard.go()
