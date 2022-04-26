import json
import time

from adafruit_clue import clue

import config
import light
import utils

time.sleep(0.5)
utils.playStartupSound(clue, config.startupSound)
display = clue.simple_text_display(colors=[config.textColour], text_scale=config.textSize)
display[0].text = "Ok"
print(json.dumps("Ok"))

while True:
 display.show()
 if clue.button_a and clue.button_b: light.lightProbe(clue, display); display[0].text="Ok"
 elif clue.button_a: utils.surfaceSensorData(clue, display, {"name": "humidity", "value": round(clue.humidity)}, config.noteDigitMappings); display[0].text="Ok"
 elif clue.button_b: utils.surfaceSensorData(clue, display, {"name": "temperature", "value": round(clue.temperature)}, config.noteDigitMappings); display[0].text="Ok"
 time.sleep(0.1)
