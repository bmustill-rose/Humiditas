import json
import time

def lightProbe(clue, display):
 print(json.dumps({'name': 'light', 'value': 'NA'}))
 display[0].text="NA"
 display.show()
 time.sleep(0.5)
 while True:
  if clue.button_a or clue.button_b: break
  clue.stop_tone()
  val = scale(sum(list(clue.color)))
  clue.start_tone(val)
  time.sleep(0.02)
 clue.stop_tone()

def scale(val):
 return round((((val - 0) * (4000 - 1000)) / (1020 - 0)) + 1000)