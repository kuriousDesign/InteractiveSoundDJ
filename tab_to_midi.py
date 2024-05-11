import mido
import time

def tab_to_midi_message(string_fret:str, velocity=64, duration=0.5):
    string, fret = string_fret[:-1], string_fret[-1]
    string_mappings = {
        'e': 40, # MIDI note number for low E string
        'B': 45, # MIDI note number for B string
        'G': 50, # MIDI note number for G string
        'D': 55, # MIDI note number for D string
        'A': 59, # MIDI note number for A string
        'E': 64  # MIDI note number for high E string
    }

    if string not in string_mappings:
        raise ValueError("Invalid string: {}".format(string))

    string_note = string_mappings[string]
    fret_number = int(fret)
    
    if fret_number < 0:
        raise ValueError("Fret number must be non-negative")

    note_number = string_note + fret_number
    return mido.Message('note_on', note=note_number, velocity=velocity, time=duration), \
           mido.Message('note_off', note=note_number, velocity=0, time=0)

# Example usage:
def send_chord(output, chord, velocity=100, duration=0.5, time_between_notes=0.1):
    for note in chord:
        note_on_msg, note_off_msg = tab_to_midi_message(note, velocity=velocity, duration=duration)
        output.send(note_on_msg)
        time.sleep(time_between_notes)
        #output.send(note_off_msg)

if __name__ == "__main__":
    output = mido.open_output("python-midi 1")
    note_on_msg, note_off_msg = tab_to_midi_message('e2', velocity=100, duration=1.0)
    #output.send(note_on_msg)   # Output: note_on channel=0 note=42 velocity=100 time=0
    #output.send(note_off_msg)  # Output: note_off channel=0 note=42 velocity=0 time=1.0

    """
    e|-2--0--4b5r4-2-0h2--2--0----------------|
    B|-4--2---------------4--2--4b5r4--2-0h2--|
    G|-4--2---------------4--2----------------| x2
    D|-4--2---------------4--2----------------|
    A|-2--0---------------2--0----------------|
    E|----------------------------------------|
    """

    chord1 = ['e2', 'B4', 'G4', 'D4', 'A2']
    chord2 = ['A0', 'D2', 'G2', 'B2', 'e0']
    chord2_reversed = chord2[::-1]

    chord3 = ['e4', 'e5', 'e4', 'e2', 'e0', 'e2']

    while True:
        strum_time = 0.05
        send_chord(output, chord1, velocity=100, duration=1.0, time_between_notes=strum_time)
        time.sleep(.7)
        send_chord(output, chord2_reversed, velocity=100, duration=1.0, time_between_notes=strum_time)
        time.sleep(1.0)
        send_chord(output, chord3, velocity=127, duration=1.0, time_between_notes=0.4)
        time.sleep(1.0)

    
    output.close()