import json
import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

def lightProbe(clue, display):
 display[0].text="NA"
 display.show()
 apds = APDS9960(board.I2C())
 apds.enable_color = True
 running = True
 while running:
  while not apds.color_data_ready:
   time.sleep(0.005)
   if clue.button_a or clue.button_b: running = False
  clue.stop_tone()
  r, g, b, c = apds.color_data
  lux = colorutility.calculate_lux(r, g, b)
  print(json.dumps({'name': 'light', 'value': lux}))
  clue.start_tone(scaleAndRound(lux))
 clue.stop_tone()

def scaleAndRound(val):
 #https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set
 #Assumes lux is between 0 and 34196.16300000001 and that we want output between A5 and B8
 return round(((val - 1) / (34196.16300000001 - 1)) * (7902 - 880) + 880)