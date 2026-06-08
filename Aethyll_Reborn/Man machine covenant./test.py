from music21 import *

# One single note
n = note.Note("C4")
n.duration.type = 'whole'

# One single measure
m = stream.Measure()
m.append(n)

# Save it
m.write('midi', fp='test.mid')
print("test.mid created! Open it in any player.")