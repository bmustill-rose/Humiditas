import time

from adafruit_clue import clue

import config
import humidity
import light
import temperature
import utils

time.sleep(0.5)
utils.playStartupSound(clue, config.startupSound)
display = clue.simple_text_display(colors=[config.textColour], text_scale=config.textSize)
display[0].text = "Ready"

while True:
 display.show()
 if clue.button_a and clue.button_b: light.lightProbe(clue, display); display[0].text="Ready"
 elif clue.button_a: humidity.humidity(clue, display, round(clue.humidity), config.noteDigitMappings); display[0].text="Ready"
 elif clue.button_b: temperature.temperature(clue, display, round(clue.temperature), config.noteDigitMappings); display[0].text="Ready"
 time.sleep(0.1)
