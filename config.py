#Humiditas configuration file


#The sequence of notes that the device plays once it is ready to use. First value is a note number and the second is a duration in MS
startupSound = [
 ('D6', 0.05),
 ('F#6', 0.05),
 ('A6', 0.05),
 ('D7', 0.1)
]

#Don't change anything below this line
notes = {
 "C6": 1046.502,
 "C#6": 1108.731,
 "D6": 1174.659,
 "D#6": 1244.508,
 "E6": 1318.51,
 "F6": 1396.913,
 "F#6": 1479.978,
 "G6": 1567.982,
 "G#6": 1661.219,
 "A6": 1760,
 "A#6": 1864.655,
 "B6": 1975.533,
 "C7": 2093.005,
 "C#7": 2217.461,
 "D7": 2349.318,
 "D#7": 2489.016,
 "E7": 2637.021,
 "F7": 2793.826,
 "F#7": 2959.955,
 "G7": 3135.964,
 "G#7": 3322.438,
 "A7": 3520,
 "A#7": 3729.31,
 "B7": 3951.066
}

#Transforms that replace note names with frequencies in the above lists so we don't have to pass around the notes dict all the time
startupSound = [(round(notes[i[0]]), i[1]) for i in startupSound]
