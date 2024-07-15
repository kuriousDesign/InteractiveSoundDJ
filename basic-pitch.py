#this is from spotify. convert mp3 to midi

from basic_pitch.inference import predict, predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH
import os

//song_path  = 'C:\\Users\\gardn\\Documents\\InteractiveSoundDJ\\suns_coming_up.mp3'
//this_dir = 'C:\\Users\\gardn\\Documents\\InteractiveSoundDJ\\'

package_share_directory = get_package_share_directory('crystal_cave_package')
music_directory = os.path.join(package_share_directory, 'resource', 'music')
song_name = "Pond.mp3"
song_path = [os.path.join(music_directory,song_name)]
output_directory = os.path.join(package_share_directory, 'midi',song_name)
os.makedirs(output_directory, exist_ok=True)

#model_output, midi_data, note_events = predict(song_path, ICASSP_2022_MODEL_PATH)
#print(midi_data.get_onsets())


# C:\Users\gardn\Documents\InteractiveSoundDJ> basic-pitch ./ ./suns_coming_up.mp3

SAVE_MIDI = True
SONIFNY_MIDI = True
SAVE_MODEL_OUTPUTS = False
SAVE_NOTES = True

predict_and_save(
    song_path,
    this_dir,
    SAVE_MIDI,
    SONIFNY_MIDI,
    SAVE_MODEL_OUTPUTS,
    SAVE_NOTES,
    ICASSP_2022_MODEL_PATH,
)