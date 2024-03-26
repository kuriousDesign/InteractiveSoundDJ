import mido
import time


class MidiControl:
    def __init__(self):
        self.output_names = mido.get_output_names()
        self.input_names = mido.get_input_names()
        self.output = mido.open_output(self.output_names[1])
        print(self.output_names[1])
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


def main():
    midi_control = MidiControl()
    time_start = time.time()
    try:
        # Perform some operations here
        # For example, send play message
        midi_control.send_play_message()
        time.sleep(1)  # Wait for 1 second
        while time.time() - 10.0 < time_start:
            
            # Send frequency message
            midi_control.send_frequency_message()
            time.sleep(.05)  # Wait for 1 second

        # Send stop message
        midi_control.send_stop_message()
        time.sleep(1)  # Wait for 1 second

    except KeyboardInterrupt:
        midi_control.close_connection()

if __name__ == "__main__":
    main()