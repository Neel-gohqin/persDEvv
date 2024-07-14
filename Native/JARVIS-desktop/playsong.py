import speech_recognition as sr
import pyttsx3
import pywhatkit
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
            # It takes microphone input from the user and returns string output

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    
                    r.pause_threshold = 1
                    #r.energy_threshold = 200
                    audio = r.listen(source)

                try:
                    
                    songlist = r.recognize_google(audio, language='en-in')
                    

                except Exception as e:
                    # print(e)
                    speak("please say that again sir...")
                    return "none"
                return songlist
            
def Music(self):
        while True:
            speak("Tell me the name of the song!")
            sng = takeCommand().lower()

            if 'moon' in sng:
                os.startfile('E:\\music_dir\\moon.mp3')

            elif 'signs' in sng:
                os.startfile('E:\\music_dir\\signs.mp3')

            else:
                pywhatkit.playonyt(sng)

            speak("Your song has been started, Enjoy Sir!")
            break