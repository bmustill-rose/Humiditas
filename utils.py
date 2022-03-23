def playStartupSound(clue, sequence):
 for note in sequence:
  clue.play_tone(note[0], note[1])