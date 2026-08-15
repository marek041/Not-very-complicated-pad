import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, LCTL
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Delay, Tap
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.LED import LED, AnimationModes
from kmk.extensions.display.ssd1306 import SSD1306

COL0 = board.GP0
COL1 = board.GP1
COL2 = board.GP2
ROW0 = board.GP3
ROW1 = board.GP7

LED_PIN = board.GP8

# busio.I2C requires explicit scl and sda keyword arguments
bus = busio.I2C(scl=board.GP_SCL, sda=board.GP_SDA)

driver = SSD1306(i2c=bus, device_address=0x3C)

display = Display(
    display=driver,
    entries=[
        TextEntry(text='Hello', x=64, y=0, x_anchor="M", scale=2)
    ],
    width=128,
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.9
)

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(display)

led = LED(
    led_pin=[LED_PIN],
    animation_mode=AnimationModes.BREATHING,
    brightness=60
)
keyboard.extensions.append(led)

keyboard.col_pins = (COL0, COL1, COL2)
keyboard.row_pins = (ROW0, ROW1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Windows Force Shutdown Macro
OFF = KC.MACRO(
    KC.LGUI(KC.R),
    KC.MACRO_SLEEP(400),
    "shutdown /s /f /t 0",
    KC.ENTER
)

FUSION = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "fusion",
    Delay(200),
    Tap(KC.ENTER)
)

buds = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "galaxy buds",
    Delay(200),
    Tap(KC.ENTER)
)

send = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "LocalSend",
    Delay(200),
    Tap(KC.ENTER)
)

keyboard.keymap = [
    [LCTL(KC.C), LCTL(KC.V), OFF],
    [FUSION,     buds,       send]
]

if __name__ == '__main__':
    keyboard.go()