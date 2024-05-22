import numpy as np
import sounddevice as sd
import numpy as np

# Constants
SAMPLE_RATE = 44100
DURATION = 1  # Duration of the note in seconds
REST_DURATION = 3  # Duration of the rest in seconds
FREQUENCY = 432  # Frequency of the note in Hz


# Calculate the number of samples for the note and rest
note_samples = int(DURATION * SAMPLE_RATE)
rest_samples = int(REST_DURATION * SAMPLE_RATE)

use_sawtooth = False
# Generate the note and rest arrays
if use_sawtooth:
    note = np.linspace(-1, 1, note_samples)
else:
    note = np.sin(2 * np.pi * FREQUENCY * np.arange(note_samples) / SAMPLE_RATE)
rest = np.zeros(rest_samples)

# Concatenate the note and rest arrays

signal = np.concatenate((note, rest))

# Play the note and rest continuouslyy
while True:
    sd.play(signal, SAMPLE_RATE)
    sd.wait()

