import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.rgb import RGB, AnimationModes

COL0 = board.D0
COL1 = board.D1
COL2 = board.D2
ROW0 = board.D3
ROW1 = board.D7

LED_PIN = board.D8 


bus = busio.I2C(scl=board.D5, sda=board.D4)

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
keyboard.extensions.append(display)

rgb = RGB(
    pixel_pin=LED_PIN,
    num_pixels=3,
    animation_mode=AnimationModes.BREATHING,
    val_limit=150,
)
keyboard.extensions.append(rgb)

keyboard.col_pins = (COL0, COL1, COL2)
keyboard.row_pins = (ROW0, ROW1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW