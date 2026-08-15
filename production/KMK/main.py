from kb import keyboard
from kmk.keys import KC, LCTL
from kmk.modules.macros import Macros, Delay, Tap

macros = Macros()
keyboard.modules.append(macros)

# Windows Force Shutdown Macro
OFF = KC.MACRO(
    KC.LGUI(KC.R),
    Delay(400),
    "shutdown /s /f /t 0",
    Delay(200),
    Tap(KC.ENTER),
)

FUSION = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "fusion",
    Delay(200),
    Tap(KC.ENTER),
)

buds = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "galaxy buds",
    Delay(200),
    Tap(KC.ENTER),
)

send = KC.MACRO(
    Tap(KC.LGUI),
    Delay(200),
    "LocalSend",
    Delay(200),
    Tap(KC.ENTER),
)

keyboard.keymap = [
    [OFF,   LCTL(KC.V), LCTL(KC.C)],
    [send,  buds,       FUSION],
]

if __name__ == '__main__':
    keyboard.go()