# code.py - "False Alarm"
# A 30 second story told with the on-board NeoPixel:
#   1. Calm   - soft blue light slowly "breathing", a quiet evening
#   2. Alarm  - sudden flashing red and white, panic!
#   3. Relief - green "all clear", then fade back to calm
# When the story ends it starts again automatically.
#
# NeoPixel setup adapted from Adafruit's example:
# https://learn.adafruit.com/adafruit-rp2040-prop-maker-feather/neopixel

import time
import board
import neopixel

# Set up the single on-board NeoPixel (from the Adafruit example)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.3

CALM = (0, 40, 120)     # soft blue: relaxed, peaceful
RED = (255, 0, 0)       # alarm light
WHITE = (255, 255, 255) # strobe flash
GREEN = (0, 255, 60)    # all clear, safe
OFF = (0, 0, 0)


def fade(start, end, seconds):
    """Slowly change the pixel from one colour to another."""
    steps = 50
    for i in range(steps + 1):
        t = i / steps  # goes from 0.0 to 1.0
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        pixel.fill((r, g, b))
        time.sleep(seconds / steps)


while True:
    # 1. CALM (10 s): slow breathing in and out, like someone resting
    for breath in range(2):
        fade(OFF, CALM, 2.5)   # breathe in
        fade(CALM, OFF, 2.5)   # breathe out

    # 2. FIRE ALARM (10 s): fast red/white flashing breaks the calm
    for flash in range(25):
        pixel.fill(RED)
        time.sleep(0.2)
        pixel.fill(WHITE)
        time.sleep(0.2)

    # 3. RELIEF (10 s): it was a false alarm - green all clear, then calm again
    pixel.fill(OFF)
    time.sleep(1)              # a moment of silence after the noise
    fade(OFF, GREEN, 2)
    time.sleep(2)              # hold the "safe" feeling
    fade(GREEN, CALM, 3)
    fade(CALM, OFF, 2)         # settle back into the quiet, and repeat
