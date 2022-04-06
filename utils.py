import json
import time

def surfaceSensorData(clue, display, data, noteDigitMappings):
 print(json.dumps(data))
 display[0].text=str(data['value'])
 display.show()
 digitsToBeeps(clue, data['value'], noteDigitMappings)

def digitsToBeeps(clue, number, mappings):
 for pos, num in enumerate(str(number)):
  repeatTone(clue, mappings[pos], int(num))

def repeatTone (clue, tone, times):
 for i in range(0, times):
  clue.play_tone(tone[0], tone[1])
  time.sleep(tone[2])

def playStartupSound(clue, sequence):
 for note in sequence:
  clue.play_tone(note[0], note[1])