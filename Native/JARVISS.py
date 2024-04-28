import sys
import time
import pyautogui
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import wikipedia
import datetime
import keyboard
import pywhatkit
import requests
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QDate,Qt
from PyQt5.QtGui import*
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from SIVRAJ import Ui_JARViss
from time import sleep
import subprocess
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import wolframalpha
import turtle



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        Ui_JARViss.terminalprint("Good Morning!")
        speak("Good Morning!")
        

    elif hour>=12 and hour<18:
        
        Ui_JARViss.terminalprint("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        
        Ui_JARViss.terminalprint("Good Evening!")
        speak("Good Evening!")

    speak("I am Jarvis Sir. please tell me how may I help you")

def WolframAlpha(Final):
        apikey = "VUKQVR-97LWXQEPY5"
        requester = wolframalpha.Client(apikey)
        requested = requester.query(Final)
            
        try:
                answer = next(requested.results).text
                return answer
        except:
                speak("value is not answerable")


class MainThread(QThread):  
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution() 
        
    def takeCommand(self):
            # It takes microphone input from the user and returns string output

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    
                    Ui_JARViss.terminalprint("Listening..")
                    r.pause_threshold = 1
                    r.energy_threshold = 100
                    audio = r.listen(source,0,9)

                try:
                    Ui_JARViss.terminalprint("Recognizing...")
                    query = r.recognize_google(audio, language='eng-in''hi')
                    Ui_JARViss.terminalprint(f" Recognizing...User said: {query}\n")

                except Exception as e:
                    return "None"
                query = query.lower()
                return query
            
    
            
    def TaskExecution(self):
        wishMe()
        while True:
                    self.query = self.takeCommand()

                #1
                    if "open notepad" in self.query:
                        path ="C:\Windows\\notepad.exe"
                        os.startfile(path)
                        
                    
                    elif 'close notepad' in self.query or 'exit notepad' in self.query or 'notepad close' in self.query or 'notepad exit' in self.query :
                        speak("ok sir")
                        os.system("taskkill /f /im notepad.exe") 
        
                         
                #2    
                    elif 'open command prompt' in self.query or 'open CMD' in self.query or 'open cmd' in self.query or 'cmd open' in self.query or 'open commandprompt' in self.query or 'command prompt open' in self.query or 'commandprompt open' in self.query or 'CMD open' in self.query:
                        speak("ok sir")
                        os.system("start cmd")
                    
                    elif 'close command prompt' in self.query or 'close CMD' in self.query or 'close cmd' in self.query or 'command prompt close' in self.query or 'commandprompt close' in self.query or 'cmd close' in self.query or 'CMD close' in self.query:
                        speak("ok sir")
                        os.system("taskkill /f /im cmd.exe")
                          
                        
                #3    
                    elif 'open vs code' in self.query or 'open vscode' in self.query or 'vs code open' in self.query or 'vscode open' in self.query :
                        speak("ok sir")
                        path ="C:\Windows\\ Microsoft VS Code"
                        os.startfile(path)
                    
                    elif 'close vs code' in self.query or 'close vscode' in self.query or 'vs code close' in self.query or 'vscode close' in self.query:
                        speak("ok sir")
                        os.system("taskkill /f /im Microsoft VS Code.exe") 
                       

                #4
                    elif 'open' in self.query:
                        from opencloseApp import openappweb
                        openappweb(self.query)
                        

                    elif 'close' in self.query or 'exit' in self.query:
                        from opencloseApp import closeappweb
                        closeappweb(self.query)

                        
                        
                #5
                    elif 'youtube search' in self.query or 'youtube' in self.query or 'search youtube' in self.query:
                            speak("OK sir, This is what i found for your search!")
                            self.query = self.query.replace("jarvis","")
                            self.query = self.query.replace("in youtube","")
                            self.query = self.query.replace("search","")
                            self.query = self.query.replace("youtube","")
                            web = 'https://www.youtube.com/results?search_query=' + self.query
                            webbrowser.open(web)
                            speak("Done sir!")
                            
                #6
                    elif 'google search' in self.query or 'google' in self.query or 'search google' in self.query:
                            speak("This is what i found for your search Sir!")
                            self.query = self.query.replace("jarvis", "")
                            self.query = self.query.replace("google","")
                            self.query = self.query.replace("in google","")
                            self.query = self.query.replace("search","")
                            pywhatkit.search(self.query)

                #7
                    elif 'stack overflow' in self.query or 'stack overflow website' in self.query:
                            speak("wait a moment")
                            webbrowser.open("stackoverflow.com")
                    
                    
                    elif 'geeks for geeks' in self.query or 'geeks for geeks website' in self.query:
                            self.query.replace("4","for")
                            speak("wait a moment")
                            webbrowser.open("geeksforgeeks.org")


                #8
                    elif 'time' in self.query:
                            hour= int(datetime.datetime.now().hour)
                            tt =time.strftime("%I:%M %p")
                            Ui_JARViss.terminalprint(tt)
                            speak(f"Sir, the time is {tt}")
                            
                #9

                    elif "weather report" in self.query or "weather forecast" in self.query:
                        search_term = self.query.split("for")[-1]
                        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-	EP-5u82AE&q=weather&oq=weather&gs_l=psy-	ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-			wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
                        webbrowser.get().open(url)
                        speak("Here is what I found for on google")


                #10
                    elif "switch the window" in self.query or "switch window" in self.query or "change window" in self.query or "change the window" in self.query:
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.keyUp("alt")
                
                
                #11   
                    elif 'wikipedia' in self.query:
                            speak('Searching Wikipedia...')
                            self.query = self.query.replace("jarvis", "")
                            self.query = self.query.replace("who is", "")
                            self.query = self.query.replace("what is", "")
                            self.query = self.query.replace("according to", "")
                            self.query = self.query.replace("wikipedia", "")
                            results = wikipedia.summary(self.query, sentences=2)
                            Ui_JARViss.terminalprint("According to Wikipedia")
                            speak("According to Wikipedia")
                            Ui_JARViss.terminalprint(results)
                            speak(results)       
                            
                               
                #12            
                    elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                        
                            speak("sir, tell me the name for the screenshot file")
                            Ui_JARViss.terminalprint("sir, tell me the name for the screenshot file")
                            name = self.takeCommand().lower()
                            Ui_JARViss.terminalprint("please hold for a few seconds")
                            speak("please hold for a few seconds, i am taking the screenshot")
                            
                            time.sleep(3)
                            img = pyautogui.screenshot()
                            img.save(f"{name}.png")
                            speak(" done sir, the screenshot is saved in our main folder")
                            
    
                    
                #13                    
                    elif '+' in self.query or '-' in self.query or '*' in self.query or '/' in self.query or 'multiply' in self.query or 'plus' in self.query or 'minues' in self.query or 'devide' in self.query or 'into' in self.query:
                        
                        Term = str(self.query)
                        Term = Term.replace("calculate","")
                        Term = Term.replace("Jarvis","")
                        Term = Term.replace("plus","+")
                        Term = Term.replace("minues","-")
                        Term = Term.replace("multiply","*")
                        Term = Term.replace("divide","/")
                        Term = Term.replace("into","*")
                        Term = Term.replace("multiplied","*")
                        
                        
                        Final = str(Term)
                        
                        try:
                            result = WolframAlpha(Final)
                            Ui_JARViss.terminalprint(f"{result}")
                            speak(result)
                        except:
                            speak("the value is not answerable")
                        
                        
                        
                    elif 'calculate' in self.query or 'calculation' in self.query:
                        speak("yes tell me the values")
                        print("yes tell me the values")
                        oprtr = self.takeCommand().lower()
                        Term = str(oprtr)
                        Term = Term.replace("calculate","")
                        Term = Term.replace("Jarvis","")
                        Term = Term.replace("plus","+")
                        Term = Term.replace("minues","-")
                        Term = Term.replace("multiply","*")
                        Term = Term.replace("divide","/")
                        Term = Term.replace("into","*")
                        Term = Term.replace("multiplied","*")

                          
                        Final = str(Term)
                        
                        try:
                            result = WolframAlpha(Final)
                            Ui_JARViss.terminalprint(f"{result}")
                            speak(result)
                        except:
                            speak("the value is not answerable")
                            

                    
                           
                #14
                    elif 'take picture' in self.query or 'click picture' in self.query or 'take a picture' in self.query or 'take photo' in self.query or 'click photo' in self.query or 'take a photo' in self.query:
                        speak("hold for a second sir")
                        keyboard.press_and_release('enter')
                    
                    
                    
                
                #15  
                    elif 'play music' in self.query:
                        from playsong import Music
                        Music(self.query)
                
                                 
                #17      
                    elif 'pause' in self.query or 'play' in self.query or 'stop' in self.query:
                        keyboard.press('k')

                    elif 'resume' in self.query or 'continue' in self.query:
                        keyboard.press('k')

                    elif 'stop' in self.query:
                        keyboard.press('k')

                    elif 'restart' in self.query:
                        keyboard.press('0')

                    elif 'mute' in self.query:
                        keyboard.press('m')

                    elif 'skip' in self.query:
                        keyboard.press('l')

                    elif 'back' in self.query:
                        keyboard.press('j')

                    elif 'full screen' in self.query or 'maximize screen' in self.query or 'maximize the screen' in self.query:
                        keyboard.press('f')

                    elif 'small screen' in self.query:
                        keyboard.press('f')
                        
                    elif 'minimize the screen' in self.query or 'minimize screen' in self.query:
                        keyboard.press('f')
                    
                    elif 'film mode' in self.query:
                        keyboard.press('t')       
                        
                    elif 'next' in self.query:
                        pyautogui.hotkey('shift','n')        
                     
                        
                #18
                    elif 'my location' in self.query or 'show my location' in self.query or 'where i am' in self.query or 'current location' in self.query:
                        speak("hold for a second sir")               
                        ip_add = requests.get('https://api.ipify.org').text
                        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        country = geo_data['country']
                        city = geo_data['city']
                        
                        Ui_JARViss.terminalprint(f"{city} {country}.")
                        webbrowser.open("https://www.google.com/maps/place/Guwahati,+Assam/@26.1429548,91.5380683,11z/data=!3m1!4b1!4m6!3m5!1s0x375a5a287f9133ff:0x2bbd1332436bde32!8m2!3d26.1157917!4d91.7085933!16zL20vMDNmeGZ5?entry=ttu")

                        speak(f"sir , You are Now in {city} {country}.")

                     
                #19    
                    elif 'find location' in self.query or 'location find' in self.query:
                        speak("tell me the location")
                        location = self.takeCommand().lower()
                        url = 'https://google.nl/maps/place/' + location + '/&amp;'
                        webbrowser.get().open(url)
                        speak("Here is your result"+ location)
                        
                            
                #20
                    elif "shutdown the system" in self.query or "turn off the system" in self.query or 'off the system' in self.query or 'off system' in self.query or ' turn off system' in self.query or 'turn off the pc' in self.query or 'shutdown the pc' in self.query or 'shutdown the computer' in self.query or 'turn off my pc' in self.query:
                        speak("have a nice day sir ")
                        os.system("shutdown /s /t 4")

                    
                    elif "restart the system" in self.query or "restart system" in self.query or 'system restart' in self.query:
                        speak("have a nice day sir ")
                        os.system("shutdown /r /t 5")
                    
                         
                    elif 'lock the system' in self.query or 'lock system' in self.query or 'lock my pc' in self.query or 'lock computer' in self.query or 'lock my computer' in self.query:
                        subprocess.call(['Rundll32.exe','user32.dll','LockWorkStation'])
                        sleep(0.2)
                
                
                    elif 'unlock it' in self.query or 'unlock' in self.query or 'unlock system' in self.query or 'unlock the system' in self.query:
                        keyboard.press_and_release('enter')
                        sleep(0.3)
                        speak("enter your pin")

                        
                #21
                    elif 'minimize all' in self.query or 'take me to desktop' in self.query or 'go to desktop' in self.query:
                        pyautogui.hotkey('win','d')
                        
                    elif 'previous window' in self.query:
                        pyautogui.hotkey('alt','tab')
                        
                
                #22 
                    elif 'left' in self.query:
                        keyboard.press_and_release('left')
                        
                    elif 'right' in self.query:
                        keyboard.press_and_release('right')  
                        
                        
                    elif 'down' in self.query:
                        keyboard.press_and_release('down')    
                        
                    elif 'up' in self.query:
                        keyboard.press_and_release('up')
                    
                    elif 'enter' in self.query or 'select' in self.query:
                        keyboard.press_and_release('enter')      
                        
                                 
                #23
                
                    elif "how are you jarvis" in self.query:
                        speak("I'm very well, thanks for asking sir ")
            
                               
                    elif "wake up" in self.query:
                        self.TaskExecution()
                        break                     
                                               
                #24     
             
             
             
#-------Connecting Ui with Backend------------             
#Threading
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
          super().__init__()
          self.ui = Ui_JARViss()
          self.ui.setupUi(self)
          self.ui.pushButton.clicked.connect(self.startTask)
          self.ui.pushButton_2.clicked.connect(self.close)
          
          #qr = self.frameGeometry()
          #cp = QDesktopWidget().availableGeometry().center()
          #qr.moveCenter(cp)
          #self.move(qr.topLeft())

          
#start and Displaying resources in gui          
    def startTask(self):
        
        self.ui.movie = QtGui.QMovie("E:/New folder/blackky.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:/New folder/8oXf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:/New folder/2RNb.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:/New folder/V3lD.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
            
        self.ui.movie = QtGui.QMovie("E:/New folder/IMG_20230509_003135.png")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:/New folder/Nt6v.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:/New folder/QNBK.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:/New folder/QNBH.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:/New folder/jvpicdcs.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        startExecution.start()
    
    #20
    def showTime(self):
        current_date = QDate.currentDate()
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser.setStyleSheet("background-color: transparent;\n"
"border:transparent;\n"
 "color:white;\n"
 "font: 700 9pt \"Segoe Script\";")
     
    def terminalprint(self,text):
        self.ui.terminalOutputBox.appendPlainText(text) 
     
            
app = QApplication(sys.argv)
Ui_JARViss= Main()
Ui_JARViss.show()
exit_code = app.exec_()
sys.exit(exit_code)