#Humiditas configuration file

noteDigitMappings = [
 ('D7', 0.1, 0.2),
 ('A7', 0.2, 0.2)
]

#The sequence of notes that the device plays once it is ready to use. First value is a note number and the second is a duration in MS
startupSound = [
 ('D6', 0.05),
 ('F#6', 0.05),
 ('A6', 0.05),
 ('D7', 0.1)
]

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
noteDigitMappings = [(notes[i[0]], i[1], i[2]) for i in noteDigitMappings]