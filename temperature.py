import utils

def temperature(clue, display, temperature, noteDigitMappings):
 display[0].text=str(temperature)
 display.show()
 utils.digitsToBeeps(clue, temperature, noteDigitMappings)