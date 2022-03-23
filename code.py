import time

from adafruit_clue import clue

import config
import humidity
import temperature
import utils

time.sleep(0.5)
utils.playStartupSound(clue, config.startupSound)

while True:
 if clue.button_a and clue.button_b: print("both")
 elif clue.button_a: humidity.humidity(clue, round(clue.humidity), config.noteDigitMappings)
 elif clue.button_b: temperature.temperature(clue, round(clue.temperature), config.noteDigitMappings)
 time.sleep(0.1)
