import time

def lightProbe(clue):
 time.sleep(0.5)
 while True:
  if clue.button_a or clue.button_b: break
  clue.stop_tone()
  val = sum(list(clue.color)) / 2.25
  clue.start_tone(val)
  time.sleep(0.02)
 clue.stop_tone()