import board
import usb_hid
from keypad import KeyMatrix
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# ===== ROWS (R1 → R5) =====
R1 = board.GP0
R2 = board.GP1
R3 = board.GP2
R4 = board.GP3
R5 = board.GP4

ROWS = (R1, R2, R3, R4, R5)

# ===== COLUMNS (C1 → C6) =====
C1 = board.GP5
C2 = board.GP6
C3 = board.GP7
C4 = board.GP8
C5 = board.GP9
C6 = board.GP10

COLS = (C1, C2, C3, C4, C5, C6)

matrix = KeyMatrix(row_pins=ROWS, column_pins=COLS)

# ===== KEYMAP (R1C1 → R5C6) =====
keymap = [
    # R1
    Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.Y,

    # R2
    Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G, Keycode.H,

    # R3
    Keycode.Z, Keycode.X, Keycode.C, Keycode.V, Keycode.B, Keycode.N,

    # R4
    Keycode.U, Keycode.I, Keycode.O, Keycode.P, Keycode.L, Keycode.SEMICOLON,

    # R5
    Keycode.LEFT_CONTROL,
    Keycode.SPACE,
    Keycode.ENTER,
    Keycode.LEFT_SHIFT,
    None,
    None,
]

# ===== MAIN LOOP =====
while True:
    event = matrix.events.get()
    if event:
        keycode = keymap[event.key_number]
        if keycode is None:
            continue

        if event.pressed:
            kbd.press(keycode)
        else:
            kbd.release(keycode)
