# autumn_lunareth_extended.py
# 11-minute final version with every golden layer we just dreamed
# Run → creates autumn_lunareth_extended.mid

from music21 import *
import random

bpm = 72
quarter = 60 / bpm
total_seconds = 11 * 60

s = stream.Score()

# Instruments (rock-solid MIDI programs)
p_celesta1 = stream.Part(); p_celesta1.insert(0, instrument.Instrument()); p_celesta1[0].midiProgram = 10   # main celesta
p_celesta2 = stream.Part(); p_celesta2.insert(0, instrument.Instrument()); p_celesta2[0].midiProgram = 10   # high shimmer
p_cello    = stream.Part(); p_cello.insert(0, instrument.Instrument());    p_cello[0].midiProgram = 42
p_violin   = stream.Part(); p_violin.insert(0, instrument.Instrument());   p_violin[0].midiProgram = 40
p_choir_m  = stream.Part(); p_choir_m.insert(0, instrument.Instrument());  p_choir_m[0].midiProgram = 52   # male choir
p_temple   = stream.Part(); p_temple.insert(0, instrument.Instrument());   p_temple[0].midiProgram = 112  # tubular bells → temple bell feel
p_rain     = stream.Part(); p_rain.insert(0, instrument.Instrument());     p_rain[0].midiProgram = 120     # reverse cymbal → rainstick

# === OPENING – double celesta descent ===
notes = ['E5','B4','G5','E5','D5','B4','G4','E4']
for i in range(16):
    for pch in reversed(notes):
        n = note.Note(pch, quarterLength=1.5)
        n.volume.velocity = 35 + i*3
        p_celesta1.append(n)
        # high shimmer on off-beats
        if i % 2 == 1:
            m = note.Note(pch, quarterLength=0.75)
            m.pitch.octave += 1
            m.volume.velocity = 30
            p_celesta2.append(m)

# === HEARTBEAT every 77 seconds (7×11) – cracked temple bell ===
for t in [77,154,231,308,385,462,539]:
    bell = note.Note('C3', quarterLength=12)
    bell.volume.velocity = 80
    p_temple.insert(t, bell)

# === AZRAEL in Morse – cello & violin duet ===
azrael_morse = ".- --.. .-. .- . .-.. "
durs = []
for c in azrael_morse:
    if c == '.': durs.append(0.5)
    elif c == '-': durs.append(1.5)
    elif c == ' ': durs.append(1.5)
durs = durs * 8

base = ['E4','F#4','G4','A4','B4','C5','D5','E5']
offset = 120
for i, dur in enumerate(durs):
    n = note.Note(base[i % len(base)], quarterLength=dur)
    n.volume.velocity = 60 + random.randint(-12,12)
    if i % 2 == 0:
        p_cello.insert(offset, n)
    else:
        p_violin.insert(offset, n)
    offset += dur

# === Male choir enters at 4:30 – long chords spelling A Z R A E L ===
choir_offset = 270
for letter, root in zip("AZRAEL", ['A3','E4','B3','F#4','C4','G4']):
    chord_notes = [root, pitch.Pitch(root).transpose('P5'), pitch.Pitch(root).transpose('P8')]
    c = chord.Chord(chord_notes, quarterLength=60)
    c.volume.velocity = 40
    p_choir_m.insert(choir_offset, c)
    choir_offset += 55

# === Rainstick from 6:00 → winter wind ===
rain_start = 360
for t in range(rain_start, total_seconds-60, 3):
    n = note.Note('C6', quarterLength=6)
    n.volume.velocity = max(10, 50 - (t-rain_start)//10)
    p_rain.insert(t, n)

# === Secret whisper at 7:47 ===
# (we’ll add this later in a DAW with a vocal sample – placeholder silence + kick heartbeat)
heartbeat = note.Note('C1', quarterLength=2)
heartbeat.volume.velocity = 90
p_cello.insert(467, heartbeat)  # 7:47

# === Final swell + long detune ===
final = chord.Chord(['E4','B4','E5','G#5','B5'], quarterLength=120)
final.volume.velocity = 70
p_violin.insert(total_seconds-180, final)

for i in range(60):
    detuned = note.Note('E6', quarterLength=4)
    detuned.pitch.microtone = i * 2
    detuned.volume.velocity = 60 - i
    p_celesta2.insert(total_seconds-200 + i*3, detuned)

# === ASSEMBLE & SAVE ===
for p in [p_celesta1, p_celesta2, p_cello, p_violin, p_choir_m, p_temple, p_rain]:
    s.insert(0, p)

print("Saving 11-minute extended Autumn…")
s.write('midi', fp='autumn_lunareth_extended.mid')
print("Done! Open autumn_lunareth_extended.mid — 11 minutes of pure golden letting-go.")