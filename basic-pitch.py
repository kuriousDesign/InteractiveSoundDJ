#this is from spotify. convert mp3 to midi

from basic_pitch.inference import predict, predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH


song_path  = 'C:\\Users\\gardn\\Documents\\InteractiveSoundDJ\\suns_coming_up.mp3'
this_dir = 'C:\\Users\\gardn\\Documents\\InteractiveSoundDJ\\'

#model_output, midi_data, note_events = predict(song_path, ICASSP_2022_MODEL_PATH)
#print(midi_data.get_onsets())


# C:\Users\gardn\Documents\InteractiveSoundDJ> basic-pitch ./ ./suns_coming_up.mp3
predict_and_save(
    song_path,
    this_dir,
    True,
    False,
    False,
    True,
    ICASSP_2022_MODEL_PATH,
)