import time

from adafruit_clue import clue

import config

while True:
 if clue.button_a and clue.button_b: print("both")
 elif clue.button_a: print("a")
 elif clue.button_b: print("b")
 time.sleep(0.3)
