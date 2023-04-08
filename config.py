#This is the Humiditas configuration file.
#When editing values in this file please pay particular attention to preserving the formatting - E.G. indentation, punctuation etc.
#If after editing this file your device becomes non-functional or functions in a way that is unexpected, simply replace it with a fresh copy from the Humiditas website, confirm that it is once again functional and attempt to make the change once again.
#Note that lines that start with the hash character (sometimes spoken as number) are comments and provide no functional purpose other than to convey supplementary information to the reader.

#Note digit mappings:
#The below values control the notes that represent tens and ones when humidity and temperature are surfaced.
#The first set of values control the tens and the second the ones.
#The format is:
# ('noteNameInQuotes', durationOfNoteInSeconds, durationOfPauseAfterNoteHasBeenPlayedInSeconds)
#Possible note values are C6 to B7 inclusive.

noteDigitMappings = [
 ('D7', 0.1, 0.2),
 ('A7', 0.2, 0.2)
]

#The startupSound is the sequence of notes that the device plays when it is ready to use.
#The format is:
# ('noteNameInQuotes', durationOfNoteInSeconds)
#Possible note values are C6 to B7 inclusive.

startupSound = [
 ('D6', 0.05),
 ('F#6', 0.05),
 ('A6', 0.05),
 ('D7', 0.1)
]

#The sleepSound is the sequence of notes that the device plays just before it goes into its powersaving mode.
#The format is:
# ('noteNameInQuotes', durationOfNoteInSeconds)
#Possible note values are C6 to B7 inclusive.

sleepSound = [
 ('D7', 0.05),
 ('A6', 0.05),
 ('F#6', 0.05),
 ('D6', 0.1)
]

#useDisplay determines if the various readings will be printed to the display or not.
#Setting the value to False increases performance and may also improve battery life.
useDisplay = True

#textColour determines the colour of the text that is printed to the display.
#Format:
#(redValue, greenValue, blueValue)
#Where the above values are between 0 and 255 inclusive.
#The default is yellow.
textColour = (255, 255, 0)

#textSize determines the size of the text that is printed to the display.
#Increase this to increase the size and decrease it to decrease it.
textSize = 15

#sleepTime determines how many seconds of inactivity causes Humiditas to enter into a deep sleep mode.
sleepTime = 60

#Don't change anything below this line
notes = {
 "C6": 1047,
 "C#6": 1109,
 "D6": 1175,
 "D#6": 1245,
 "E6": 1319,
 "F6": 1397,
 "F#6": 1480,
 "G6": 1568,
 "G#6": 1661,
 "A6": 1760,
 "A#6": 1865,
 "B6": 1976,
 "C7": 2093,
 "C#7": 2217,
 "D7": 2349,
 "D#7": 2489,
 "E7": 2637,
 "F7": 2794,
 "F#7": 2960,
 "G7": 3136,
 "G#7": 3322,
 "A7": 3520,
 "A#7": 3729,
 "B7": 3951
}

#Transforms that replace note names with frequencies in the above lists so we don't have to pass around the notes dict all the time
startupSound = [(notes[i[0]], i[1]) for i in startupSound]
sleepSound = [(notes[i[0]], i[1]) for i in sleepSound]
noteDigitMappings = [(notes[i[0]], i[1], i[2]) for i in noteDigitMappings]