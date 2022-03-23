def playStartupSound(clue, sequence):
 print(sequence)
 for note in sequence:
  clue.play_tone(note[0], note[1])