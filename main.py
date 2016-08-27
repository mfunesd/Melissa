import sys
import yaml
import speech_recognition as sr

from GreyMatter import play_music
from brain import brain
from GreyMatter.SenseCells.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
music_path = profile_data['music_path']

#play_music.mp3gen(music_path)

tts('Hola ' + name + ', me alegro de estar contigo otra vez') #+ ', systems are now ready to run. How can I help you?')

def main():
    print("***********************************************************")
    print("* PLEASE IGNORE THE ERROR MESSAGES, THEY AREN'T A PROBLEM *")
    print("***********************************************************")

    r = sr.Recognizer()
    r.energy_threshold = 4000

    while True:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio).lower().replace("'", "")
            print("Melissa thinks you said '" + speech_text + "'")
        except sr.UnknownValueError:
            print("Melissa could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
        brain(name, speech_text, music_path, city_name, city_code)

main()
