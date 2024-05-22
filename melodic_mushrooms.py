import cv2
import mediapipe as mp
import numpy as np
import rtmidi
from rtmidi.midiconstants import (CONTROL_CHANGE)
import time
import random
#from interactive_dj import *
import numpy as np
import sounddevice as sd
from dubstep import *

#midiout = rtmidi.MidiOut()
#interactive_dj = InteractiveDJ()


# WEBCAM SETUP
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

def convert_range(value, in_min, in_max, out_min, out_max):
    l_span = in_max - in_min
    r_span = out_max - out_min
    scaled_value = (value - in_min) / l_span
    scaled_value = out_min + (scaled_value * r_span)
    return np.round(scaled_value)



def make_note(pitch, note_on, note_off):
    duration = note_off - note_on
    t = np.linspace(0, duration, int(duration * 44100), endpoint=False)
    frequency = 440 * 2 ** ((pitch - 69) / 12)
    waveform = np.sin(2 * np.pi * frequency * t)
    sd.play(waveform, samplerate=44100, blocking=True)

def send_notes(pitch=60, repeat=1):
    for i in range(repeat):
        note_on = [0x90, pitch, 112]
        note_off = [0x80, pitch, 0]
        #midiout.send_message(note_on)
        time.sleep(random.uniform(0.1, 0.8))
        #midiout.send_message(note_off)

def send_mod(cc=1, value=0):
    mod1 = ([CONTROL_CHANGE | 0, cc, value])
    print(value)
    if value > 0.0:
        #midiout.send_message(mod1)
        pass

def run():
    while True:
        # Capture frame-by-frame
        success, img = cap.read()
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, c = img.shape

        # Drawing lines and such
        img = cv2.rectangle(img, (0, 0), (int(w/2), 270), (64, 224, 208), 2)
        img = cv2.rectangle(img, (0, 0), (int(w/2), 540), (64, 224, 208), 2)
        img = cv2.rectangle(img, (0, 0), (int(w/2), 810), (64, 224, 208), 2)
        img = cv2.rectangle(img, (0, 0), (int(w/2), 1080), (64, 224, 208), 2)
        # Right side
        img = cv2.rectangle(img, (int(w/2), int(h/2)), (w, 0), (164, 24, 208), 2)
        img = cv2.rectangle(img, (int(w / 2), int(h)), (w, int(h/2)), (164, 24, 28), 2)
        # Text
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.putText(img, 'Note 1', (10, h - 18), font, 0.9, (255, 200, 5), 4, cv2.LINE_AA)
        img = cv2.putText(img, 'Note 2', (10, h - 290), font, 0.9, (255, 200, 5), 4, cv2.LINE_AA)

        img = cv2.putText(img, 'Note 3', (400, h - 18), font, 0.9, (255, 200, 5), 4, cv2.LINE_AA)
        img = cv2.putText(img, 'Note 4', (400, h - 290), font, 0.9, (255, 200, 5), 4, cv2.LINE_AA)

        results = hands.process(imgRGB)

        fundamental_freq = 432

        if results.multi_hand_landmarks:
            print(len(results.multi_hand_landmarks))
            for hand_landmarks in results.multi_hand_landmarks:
                pink_x = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].x
                pink_y = hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y 

                print("pinky: ", pink_y*h)

                if pink_x < 0.5:
                    if round(pink_y * h) in range(262, 524):
                        make_dubstep_note(fundamental_freq*1)
                    if round(pink_y * h) in range(1, 261):
                        make_dubstep_note(fundamental_freq*1.5)
                elif pink_x > 0.5:
                    if round(pink_y * h) in range(262, 524):
                        make_dubstep_note(fundamental_freq*1.75)
                    if round(pink_y * h) in range(1, 261):
                        make_dubstep_note(fundamental_freq*2)
                else:
                    print('Outside Range')
                mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)
        fps = 1
        cv2.imshow("My face", img)
        cv2.waitKey(fps)

run()