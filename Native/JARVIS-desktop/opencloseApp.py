import os
import pyttsx3
import webbrowser
import pyautogui
import speech_recognition as sr
from time import sleep
import pywhatkit



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
                    audio = r.listen(source,0,8)

                try:
  
                    srcch = r.recognize_google(audio, language='en-in')

                except Exception as e:
                    # print(e)
                    speak("please say that again...")
                    
                    return ""
                return srcch
  
                     ###5_Open/Close_Apps and web 
                                   
dictapp = {"word":"winword","chrome":"chrome","powerpoint":"powerpnt", "browser":"msedge"}


def openappweb(self):
    
    speak("wait a moment sir")
    
    if '.com' in self or '.co.in' in self or '.org' in self:
        self = self.replace("open","")
        self.replace("jarvis","")
        self.replace("launch","")
        webbrowser.open(f"https://www.{self}")
    
    
    
    elif 'youtube' in self :
        while True:
            webbrowser.open("youtube.com")
            sleep(1)
            speak("what you will like to watch")
            srrchh = takeCommand().lower()
            try: 
                pywhatkit.playonyt(f"{srrchh}")
                break
            except Exception as e:
                speak("say again")
                break  
            

    elif 'facebook' in self:
        webbrowser.open("facebook.com")
    
    
    
    elif 'google maps' in self or 'google map' in self:
        webbrowser.open("https://www.google.co.in/maps")
    
    
    
    elif 'google' in self:
        while True:
            webbrowser.open("google.com")
            sleep(0.9)
            speak("what will i search for")
            srrchh = takeCommand().lower()
            try: 
                pywhatkit.search(f"{srrchh}")
                break
            except Exception as e:
                speak("say again")
                break
            
    
    elif 'geeks for geeks' in self or 'geeks for geeks website' in self or 'geeks for geek' in self or 'geeks for geek website' in self:
        self.replace("4","for")
        webbrowser.open("geeksforgeeks.org")

    
    elif 'camera' in self:
        pyautogui.press("super")
        pyautogui.typewrite("camera")
        pyautogui.sleep(0.2)
        pyautogui.press("enter")
    
    
    elif 'mail' in self or 'email' in self:
        pyautogui.press("super")
        pyautogui.typewrite("mail")
        pyautogui.sleep(0.2)
        pyautogui.press("enter")
    
                    
        
    elif 'stack overflow' in self or 'stack overflow website' in self:
        webbrowser.open("stackoverflow.com")
    
    
    elif 'file explorer' in self or 'this pc' in self or 'storage'in self:
        pyautogui.hotkey('win','e')
        
        
    else:
            keys = list(dictapp.keys())
            for app in keys:
                if app in self:
                        os.system(f"start {dictapp[app]}")
            
                
def closeappweb(self):
    speak("ok sir")
    
    if "one tab" in self:
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
    
    elif "the tab" in self or "first tab" in self or "number 1 tab" in self or "recent tab" in self:
        pyautogui.hotkey("ctrl","1")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
         
    elif "number 2 tab" in self or "second tab" in self:
        pyautogui.hotkey("ctrl","2")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
    
    elif "2 tab" in self or "2 tabs" in self:
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        
    elif "number three tab" in self or "third tab" in self or " number 3 tab" in self:
        pyautogui.hotkey("ctrl","3")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")   
    
    elif "3 tab" in self or "three tabs" in self:
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
    
    
    elif "number four tab" in self or "fourth tab" in self or " number 4 tab" in self:
        pyautogui.hotkey("ctrl","4")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")  
    
        
    elif "4 tab" in self or "four tab" in self or "4 tabs" in self:
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
    
    elif "5 tab" in self or "five tab" in self or "5 tabs" in self:
        
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)
        pyautogui.hotkey("ctrl","w")
        sleep(0.4)

        
    elif "facebook" in self:
        
        os.system("taskkill /f /im msedge.exe")
        sleep(0.5)

    
    elif "google" in self:
        
        os.system("taskkill /f /im msedge.exe")
        sleep(0.5)
        
        
    elif "youtube" in self:

        os.system("taskkill /f /im msedge.exe")
        sleep(0.5)
    
    
    elif "camera" in self: 
           
        pyautogui.hotkey("alt","f4")
        sleep(0.4)


    elif "this pc" in self: 
           
        pyautogui.hotkey("alt","f4")
        sleep(0.4)
    
    
    elif "mail" in self or "email" in self: 
           
        pyautogui.hotkey("alt","f4")
        sleep(0.4)
            
        
    elif 'google map' in self or 'google maps' in self:
        os.system("taskkill /f /im msedge.exe")

    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in self:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
