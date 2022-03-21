#Humiditas configuration file

#A list of notes that the tuner function will play
tunerNotes = ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']

#The sequence of notes that the device plays once it is ready to use. First value is a note number and the second is a duration in MS
startupSound = [
 ('E2', 50),
 ('A2', 50),
 ('D3', 50),
 ('G3', 50),
 ('B3', 50),
 ('E4', 100)
]

#Don't change anything below this line
notes = {
 "C2": 65.406,
 "C#2": 69.296,
 "D2": 73.416,
 "D#2": 77.782,
 "E2": 82.407,
 "F2": 87.307,
 "F#2": 92.499,
 "G2": 97.999,
 "G#2": 103.826,
 "A2": 110,
 "A#2": 116.541,
 "B2": 123.471,
 "C3": 130.813,
 "C#3": 138.591,
 "D3": 146.832,
 "D#3": 155.563,
 "E3": 164.814,
 "F3": 174.614,
 "F#3": 184.997,
 "G3": 195.998,
 "G#3": 207.652,
 "A3": 220,
 "A#3": 233.082,
 "B3": 246.942,
 "C4": 261.626,
 "C#4": 277.183,
 "D4": 293.665,
 "D#4": 311.127,
 "E4": 329.628,
 "F4": 349.228,
 "F#4": 369.994,
 "G4": 391.995,
 "G#4": 415.305,
 "A4": 440,
 "A#4": 466.164,
 "B4": 493.883
}

#Transforms that replace note names with frequencies in the above lists so we don't have to pass around the notes dict all the time
startupSound = [(notes[i[0]], i[1]) for i in startupSound]
tunerNotes = [notes[i] for i in tunerNotes]