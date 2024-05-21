import numpy as np
import scipy.signal
import sounddevice as sd
import time
import rclpy
from rclpy.node import Node

# Parameters
sample_rate = 44100  # Samples per second
duration = .2       # Duration in seconds
#frequency = 50       # Base frequency of the bass
#lfo_frequency = 1    # Frequency of the LFO in Hz
lfo_depth = 0.5      # Depth of the LFO modulation (0 to 1)



class SoundMaker(Node):
    def __init__(self):
        super().__init__('sound_maker')
        self.sample_rate = 44100
        self.duration = 0.2
        self.lfo_depth = 0.5

    def make_dubstep_note(self, frequency, lfo_frequency=1.0):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        saw_wave = scipy.signal.sawtooth(2 * np.pi * frequency * t)
        lfo = np.sin(2 * np.pi * lfo_frequency * t)
        modulated_wave = saw_wave * (1 + self.lfo_depth * lfo)
        cutoff_freq = 200.0
        nyquist = 0.5 * self.sample_rate
        normal_cutoff = cutoff_freq / nyquist
        b, a = scipy.signal.butter(1, normal_cutoff, btype='low', analog=False)
        filtered_wave = scipy.signal.filtfilt(b, a, modulated_wave)
        filtered_wave = np.int16(filtered_wave / np.max(np.abs(filtered_wave)) * 32767)
        silence_duration = 3.0
        silence_samples = int(self.sample_rate * silence_duration)
        silence = np.zeros(silence_samples)
        combined_wave = np.concatenate((filtered_wave, silence))
        print("note_freq: ", frequency)
        sd.play(combined_wave, self.sample_rate)
        sd.wait()

    def main(self):
        note_freq = 432.0
        lfo_freq = 1.0
        while True:
            self.make_dubstep_note(note_freq, lfo_freq)
            time.sleep(1.0)
            note_freq *= 2
            if note_freq > 5000:
                note_freq = 432.0
                lfo_freq = 1.0

def main(args=None):
    rclpy.init(args=args)
    node = SoundMaker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()



def make_dubstep_note(frequency, lfo_frequency=1.0):
    # Time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate sawtooth waveform
    saw_wave = scipy.signal.sawtooth(2 * np.pi * frequency * t)

    # Generate LFO (low-frequency oscillator)
    lfo = np.sin(2 * np.pi * lfo_frequency * t)

    # Apply LFO to modulate the amplitude
    modulated_wave = saw_wave * (1 + lfo_depth * lfo)

    # Apply low-pass filter
    cutoff_freq = 200.0  # Cutoff frequency in Hz
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = scipy.signal.butter(1, normal_cutoff, btype='low', analog=False)
    filtered_wave = scipy.signal.filtfilt(b, a, modulated_wave)

    # Normalize to 16-bit range
    filtered_wave = np.int16(filtered_wave / np.max(np.abs(filtered_wave)) * 32767)
    # Create silence
    silence_duration = 3.0  # Duration of silence in seconds
    silence_samples = int(sample_rate * silence_duration)
    silence = np.zeros(silence_samples)

    # Combine filtered_wave and silence
    #combined_wave = np.concatenate((filtered_wave, silence))
    print("note_freq: ", frequency)
    sd.play(filtered_wave, sample_rate)
    sd.wait()
    #return combined_wave


def main():
    # Play combined sound
    note_freq = 432.0
    lfo_freq = 1.0
    while True:
        make_dubstep_note(note_freq, lfo_freq)
        time.sleep(1.0)

        note_freq *= 2
        if note_freq > 5000:
            note_freq = 432.0
            lfo_freq = 1.0

if __name__ == "__main__":
    main()
