import sys

import yaml
import speech_recognition as sr

from brain import brain
from GreyMatter.SenseCells.tts import tts

profile = open('GreyMatter/profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']

tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')

def main():

    def callback(recognizer, audio):

        # received audio data, now we'll recognize it using Google Speech Recogniti$
        try:
            # save to file
            # with open("microphone-results.wav", "wb") as f:
            #     f.write(audio.get_wav_data())
            # define message for tts
            message = recognizer.recognize_google(audio)
            tts(message)
            brain(name, message)
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SP$
            # instead of `r.recognize_google(audio)`
            print("Melissa thinks you said '" + message + "'")
        except sr.UnknownValueError:
            print("Melissa could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source) # we only need to calibrate once, before$
        print("Say something!")
    # start listening in the background (note that we don't have to do this inside $
    stop_listening = r.listen_in_background(m, callback)
    # `stop_listening` is now a function that, when called, stops background listen$

    # do some other computation for 5 seconds, then stop listening and keep doing o$

    import time
    for _ in range(50): time.sleep(0.1) # we're still listening even though the mai$
    stop_listening() # calling this function requests that the background listener $
    #while True: time.sleep(0.1)

main()
