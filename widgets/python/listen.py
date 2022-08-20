#!/usr/bin/python3

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
freq = 44100
duration = 2
while True:
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)
    sd.wait()
    write("16-122828-0002b.wav", freq, recording)
    wv.write("16-122828-0002.wav", recording, freq, sampwidth=2)
    import speech_recognition as sr
    filename = "16-122828-0002.wav"
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)



# # [How to Convert Speech to Text in Python - Python Code](https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python)
# # $ pip3 install sounddevice
# # $ pip3 install wavio
# # $ pip3 install scipy
# # import required libraries
# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv
# # Sampling frequency
# freq = 44100

# # Recording duration
# duration = 2
# # Start recorder with the given values of 
# # duration and sample frequency
# recording = sd.rec(int(duration * freq), 
#                    samplerate=freq, channels=2)

# # Record audio for the given number of seconds
# sd.wait()
# # This will convert the NumPy array to an audio
# # file with the given sampling frequency
# write("16-122828-0002b.wav", freq, recording)
# # Convert the NumPy array to audio file
# wv.write("16-122828-0002.wav", recording, freq, sampwidth=2)












# # [Create a Voice Recorder using Python - GeeksforGeeks](https://www.geeksforgeeks.org/create-a-voice-recorder-using-python/)
# # pip3 install SpeechRecognition pydub
# import speech_recognition as sr
# filename = "16-122828-0002.wav"
# # initialize the recognizer
# r = sr.Recognizer()
# # open the file
# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)
