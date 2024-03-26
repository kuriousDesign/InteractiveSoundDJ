from osc_client import *
from midi_control import *
import time
from enum import Enum



class OSC_CLIENTS(Enum):
    WAVEFORM = "waveform"
    ABLETON = "ableton"

class InteractiveDJ:
    def __init__(self, osc_client = OSC_CLIENTS.WAVEFORM):
        if osc_client == OSC_CLIENTS.WAVEFORM:
            self.osc_client = WaveformOscControl()
        else:
            self.osc_client = AbletonOscControl()

        self.midi_control = MidiControl()

    def start_song(self):
        self.osc_client.start_transport()

    def affect_frequency(self):
        time_start = time.time()
        while time.time() - 10.0 < time_start:
            self.midi_control.send_frequency_message()
            time.sleep(.05)

    def stop_song(self):
        self.osc_client.stop_transport()

    def play(self):
        self.start_song()
        self.affect_frequency()
        self.stop_song()


if __name__ == "__main__":
    interactive_dj = InteractiveDJ()
    interactive_dj.play()