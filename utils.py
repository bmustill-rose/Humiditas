import time

def splitNumber(num):
 from collections import OrderedDict
 return OrderedDict([
  ('thousands', (num // 1000) % 10),
  ('hundreds', (num // 100) % 10),
  ('tens', (num // 10) % 10),
  ('ones', num % 10)
   ])

def surfaceSensorData(clue, display, data, noteDigitMappings):
 if display:
  display[0].text=str(data['value'])
  display.show()
  time.sleep(0.005)
 digitsToBeeps(clue, data['value'], noteDigitMappings)
 print(data)

def digitsToBeeps(clue, number, mappings):
 split = splitNumber(number)
 for units, number in split.items():
  repeatTone(clue, mappings[units], number)

def repeatTone (clue, toneData, times):
 for i in range(0, times):
  clue.play_tone(toneData[0], toneData[1])
  time.sleep(toneData[2])

def playSoundSequence(clue, sequence):
 for note in sequence:
  clue.play_tone(note[0], note[1])

def goToSleep(clue, sleepSound):
 import alarm
 import board
 playSoundSequence(clue, sleepSound)
 #Have to deinit the buttons before they can be used to wake from alarms
 clue._a.deinit()
 clue._b.deinit()
 paa = alarm.pin.PinAlarm(pin=board.BUTTON_A, value=False, pull=True) 
 pab = alarm.pin.PinAlarm(pin=board.BUTTON_B, value=False, pull=True) 
 alarm.exit_and_deep_sleep_until_alarms(paa, pab)