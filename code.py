import json
import time

from adafruit_clue import clue

import config
import light
import utils

display = clue.simple_text_display(colors=[config.textColour], text_scale=config.textSize) #Have to init and blit the display even if we don't want to use it to prevent REPL output being shown
if config.useDisplay: display[0].text = "Ok"
time.sleep(0.5)
utils.playSoundSequence(clue, config.startupSound)
print(json.dumps("Ok"))

while True:
 display.show()
 if clue.button_a and clue.button_b:
  light.lightProbe(clue, display if config.useDisplay else None);
  if config.useDisplay: display[0].text = "Ok"
 elif clue.button_a: 
  utils.surfaceSensorData(clue, display if config.useDisplay else None, {"name": "humidity", "value": round(clue.humidity)}, config.noteDigitMappings)
  if config.useDisplay: display[0].text = "Ok"
 elif clue.button_b:
  utils.surfaceSensorData(clue, display if config.useDisplay else None, {"name": "temperature", "value": round(clue.temperature)}, config.noteDigitMappings)
  if config.useDisplay: display[0].text = "Ok"
 time.sleep(0.05)