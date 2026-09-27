# False Alarm

A 30-second light story told with one pixel, the on-board NeoPixel of the
Adafruit RP2040 Prop-Maker Feather, written in CircuitPython.

## The story
1. **Calm:** soft blue light slowly breathing in and out
2. **Fire alarm:** sudden fast red and white flashing
3. **Relief:** darkness, a green "all clear", then back to calm

The sequence loops forever.

## How to run
1. Install CircuitPython on the board and add the `neopixel` library to `lib/`.
2. Copy `code.py` to the CIRCUITPY drive.
3. It starts automatically.

## Credits
NeoPixel setup adapted from Adafruit's guide:
https://learn.adafruit.com/adafruit-rp2040-prop-maker-feather/neopixel
