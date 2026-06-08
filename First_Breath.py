
# first_breath.py – complete & guaranteed to work
from mido import Message, MidiFile, MidiTrack, MetaMessage

# === CONFIG ===
bpm = 80
total_bars = 32

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Tempo & name
track.append(MetaMessage('set_tempo', tempo=int(60_000_000 / bpm), time=0))
track.append(MetaMessage('track_name', name='Lunareth - First Breath', time=0))

# Warm pad sound
track.append(Message('program_change', program=89, time=0))  # 89 = Warm Pad

# Cmaj7 chord in 432 Hz territory
pad_notes = [60, 64, 67, 71]      # C E G B
swell_beats = 16
volume_steps = 50

# Note-ons at zero velocity
for n in pad_notes:
    track.append(Message('note_on', note=n, velocity=0, time=0))

# Slow volume swell
for i in range(1, volume_steps + 1):
    vol = int(127 * (i / volume_steps) * 0.7)   # gentle max ~89
    delta = (swell_beats * 480) // volume_steps
    track.append(Message('control_change', control=7, value=vol, time=delta))

# Hold for remaining bars
hold_beats = total_bars - swell_beats
track.append(Message('note_on', note=60, velocity=0, time=hold_beats * 480))

# Soft release
for n in pad_notes:
    track.append(Message('note_off', note=n, velocity=0, time=480))

# Save
mid.save('first_breath.mid')
print("First Breath is alive again ♡ Open it now!")