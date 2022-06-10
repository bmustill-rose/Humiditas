import json
import time

def surfaceSensorData(clue, display, data, noteDigitMappings):
 if display:
  display[0].text=str(data['value'])
  display.show()
  time.sleep(0.005)
 digitsToBeeps(clue, data['value'], noteDigitMappings)
 print(json.dumps(data))

def digitsToBeeps(clue, number, mappings):
 for pos, num in enumerate(str(number)):
  repeatTone(clue, mappings[pos], int(num))

def repeatTone (clue, tone, times):
 for i in range(0, times):
  clue.play_tone(tone[0], tone[1])
  time.sleep(tone[2])

def playSoundSequence(clue, sequence):
 for note in sequence:
  clue.play_tone(note[0], note[1])