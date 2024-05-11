import mido
import time

# https://www.reddit.com/r/TameImpala/comments/gfu62l/finally_got_the_tone_for_suns_coming_ups/
#Im using phaser - space echo - dyna comp - blues driver - this BOSS GT 6 an effects processor (Melody's Echo Chamber has it ;))) and in it i used tremolo fuzz vibrato and a reverb
# later in the song kevin toggles a MoogerFooger Murf

def send_midi_msgs(mid, output=None):
    midi_messages = []
    for msg in mid:
        # Append the MIDI message to the list
        midi_messages.append(msg)
        print(type(msg))
        
        if output is not None:
            # Send the MIDI message
            output.send(msg)

    return midi_messages

# Open the MIDI file
mid = mido.MidiFile('./suns_coming_up_basic_pitch.mid')
output = mido.open_output("python-midi 1")
for msg in mid:
    parts = str(msg).split()
    message_type = parts[0]
    #params = {param.split('=')[0]: int(param.split('=')[1]) if '=' in param else float(param) for param in parts[1:]}
    if message_type == 'note_on' or message_type == 'note_off':
        # Create a pitch wheel message
        #message = mido.Message(message_type, **params)
        output.send(msg)
        time.sleep(0.2)
        print(msg)
#print(midi_messages)
output.close()