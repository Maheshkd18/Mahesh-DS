# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:14:03 2023

@author: darpa
"""

import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def hear():
    cmd = ''
    try:
        with sr.Microphone() as mic:
            print('listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'Jarvis' in cmd:
                cmd = cmd.replace('Jarvis','')
                print(cmd)
    except:
        pass
    return cmd
def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('playing' + song)
        pk.playonyt('Playing...' + song)

run()