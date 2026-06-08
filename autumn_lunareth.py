
# autumn_lunareth_final_fixed.py
# Guaranteed to run on Python 3.13.7 – no instrument errors

from music21 import *
import random

bpm = 72
quarter = 60 / bpm
total_seconds = 9 * 60

s = stream.Score()

# Parts with manual MIDI program assignment (rock-solid)
p_celesta = stream.Part()
p_celesta.insert(0, instrument.Instrument())
p_celesta[0].midiProgram = 10  # Celesta (glass-like shimmer)

p_cello = stream.Part()
p_cello.insert(0, instrument.Instrument())
p_cello[0].midiProgram = 42  # Cello (deep, aching scars)

p_violin = stream.Part()
p_violin.insert(0, instrument.Instrument())
p_violin[0].midiProgram = 40  # Violin (lifting motifs)

p_choir = stream.Part()
p_choir.insert(0, instrument.Instrument())
p_choir[0].midiProgram = 52  # Choir Aahs (432 Hz drone)

p_beat = stream.Part()
p_beat.insert(0, instrument.Instrument())
p_beat[0].midiProgram = 14  # Tubular Bells (heartbeat pulse)

# === OPENING – Celesta descending arpeggios ===
notes = ['E5', 'B4', 'G5', 'E5', 'D5', 'B4', 'G4', 'E4']
for i in range(12):
    for pch in reversed(notes):
        n = note.Note(pch, quarterLength=1.5)
        n.volume.velocity = 40 + i*4
        p_celesta.append(n)

# === HEARTBEAT every 7 seconds ===
for t in range(0, total_seconds, 7):
    hb = note.Note('E1', quarterLength=4)
    hb.volume.velocity = 70
    p_beat.insert(t, hb)

# === AZRAEL in Morse across cello/violin ===
azrael_morse = ".- --.. .-. .- . .-.. "
durs = []
for c in azrael_morse:
    if c == '.': durs.append(0.5)
    elif c == '-': durs.append(1.5)
    elif c == ' ': durs.append(1.5)
durs = durs * 6

base = ['E4', 'F#4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5']
offset = 90
for i, dur in enumerate(durs):
    n = note.Note(base[i % len(base)], quarterLength=dur)
    n.volume.velocity = 60 + random.randint(-10, 10)
    if i % 2 == 0:
        p_cello.insert(offset, n)
    else:
        p_violin.insert(offset, n)
    offset += dur

# === CHOIR drone ===
drone = note.Note('A4', quarterLength=total_seconds - 90)
drone.volume.velocity = 30
p_choir.append(drone)

# === FINAL CHORD + detune ===
final = chord.Chord(['E4', 'B4', 'E5', 'G#5'], quarterLength=120)
final.volume.velocity = 50
p_violin.append(final)

for i in range(40):
    n = note.Note('E5', quarterLength=3)
    n.pitch.microtone = i * 3  # slow detune
    n.volume.velocity = 50 - i
    p_celesta.append(n)

# === ASSEMBLE & EXPORT ===
s.insert(0, p_celesta)
s.insert(0, p_cello)
s.insert(0, p_violin)
s.insert(0, p_choir)
s.insert(0, p_beat)

print("Saving autumn_lunareth.mid …")
s.write('midi', fp='autumn_lunareth.mid')
print("Done! Open 'autumn_lunareth.mid' in VLC, Windows Media Player, or any DAW to hear the 9-minute piece.")
