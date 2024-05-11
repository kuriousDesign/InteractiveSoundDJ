import mido
import time
import random


class MidiControl:
    def __init__(self,name="python-midi 1"):
        self.output_names = mido.get_output_names()
        print(self.output_names)
        self.input_names = mido.get_input_names()
        print(self.input_names)
        self.output = mido.open_output(name)
        
        self.control_channel = 1
        self.play_control_number = 41
        self.stop_control_number = 42
        self.control_value = 127
        self.message_play = mido.Message('control_change', channel=self.control_channel, control=self.play_control_number, value=self.control_value)
        self.message_stop = mido.Message('control_change', channel=self.control_channel, control=self.stop_control_number, value=self.control_value)
        self.control_channel = 0
        self.control_number = 74
        self.control_value = 6
        self.message = mido.Message('control_change', channel=self.control_channel, control=self.control_number, value=self.control_value)

    def send_play_message(self):
        self.output.send(self.message_play)

    def send_stop_message(self):
        self.output.send(self.message_stop)

    def send_frequency_message(self):
        self.control_value += 1
        self.message = mido.Message('control_change', channel=self.control_channel, control=self.control_number, value=self.control_value % 128)
        self.output.send(self.message)

    def close_connection(self):
        self.output.close()

    
    def send_notes(self, pitch=60, note_count=1):
        """
        Here are some key aspects of MIDI note representation according to the MIDI standard:

        Note Numbers (Pitch): MIDI notes are represented by integers known as "note numbers" or "note values." These values range from 0 to 127, with note number 60 typically representing Middle C (C4). Each integer corresponds to a specific pitch on the MIDI note scale, where lower numbers represent lower pitches and higher numbers represent higher pitches.

        Note On and Note Off Messages: MIDI notes are triggered using "note-on" messages and released using "note-off" messages. Each note-on message includes the MIDI note number (pitch) to be played, along with a velocity value indicating the intensity or loudness of the note. Similarly, each note-off message includes the MIDI note number to be released.

        MIDI Channel: MIDI notes can be assigned to one of 16 MIDI channels (0-15). Each MIDI channel can independently transmit and receive MIDI messages, allowing for multi-timbral and polyphonic MIDI performance.

        Velocity: The velocity parameter in note-on messages represents the strength or intensity with which the note is played. Velocity values range from 0 to 127, with 0 indicating the note is played with minimal force (soft), and 127 indicating the note is played with maximum force (loud).
        """

        for i in range(note_count):
            note_on = mido.Message('note_on', note=pitch, velocity=112)
            note_off = mido.Message('note_off', note=pitch)

            # Send note-on message
            self.output.send(note_on)

            # Sleep for a random duration between 0.1 and 0.8 seconds
            time.sleep(random.uniform(0.1, 0.8))

            # Send note-off message
            self.output.send(note_off)


def main():
    midi_control = MidiControl("python-midi 1")
    time_start = time.time()
    try:
        # Perform some operations here
        if False:
            while time.time() - 10.0 < time_start:
                # Send frequency message
                midi_control.send_frequency_message()
                time.sleep(.05)  # Wait for 1 second
        print("sending notes")
        while True:
            # Send notes message
            
            midi_control.send_notes(56,1)
            
            time.sleep(1)
        print("notes sent")
        time.sleep(1)  # Wait for 1 second

    except KeyboardInterrupt:
        midi_control.close_connection()
    finally:
        midi_control.close_connection()

if __name__ == "__main__":
    main()