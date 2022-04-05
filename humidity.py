import utils

def humidity(clue, display, humidity, noteDigitMappings):
 display[0].text=str(humidity)
 display.show()
 utils.digitsToBeeps(clue, humidity, noteDigitMappings)