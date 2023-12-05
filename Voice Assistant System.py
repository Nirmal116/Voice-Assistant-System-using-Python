from tkinter import messagebox
import tkinter
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from datetime import date
window = tkinter.Tk()
window.geometry('720x640')
def clicked():



    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishme():
        hour = int(datetime.datetime.now().hour)

        if (hour >= 0 and hour <= 12):
            speak("Good Morning")
        elif hour >= 12 and hour < 18:
            speak('Good Afternoon')
        else:
            speak("Good evening")
        print("tell me what to do")
        speak("tell me what to do")

    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            print("Recognizing your voice...")
            query = r.recognize_google(audio, language="en-in")
            print(f"My dear friend you said :{query}\n")

        except Exception as e:
            speak("say that again please...")
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("20BIT4063@mkce.ac.in", '20BIT40631505')
        server.sendmail("20BIT4063@mkce.ac.in", 'nirmal012003@gmail.com', content)
        server.quit()

    if __name__ == '__main__':
        wishme()
        while True:
            query = takecommand().lower()
            if 'open wikipedia' in query:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open notepad' in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            elif 'open youtube' in query:
                webbrowser.open('youtube.com')
            elif 'open whatsapp' in query:
                webbrowser.open('whatsapp.com')


            elif 'open google' in query:
                webbrowser.open('google.com')

            elif 'date' in query:

                a1 = datetime.datetime.now()
                print(a1)
                a = date.today()
                speak(a)

            elif 'open village cooking channel' in query:
                webbrowser.open('https://www.youtube.com/results?search_query=village+cooking+channel')
            elif 'open linkedIn' in query:
                webbrowser.open("www.linkedIn.com")
            elif 'open calculator' in query:
                cam = "C:\\Windows\\System32\\calc.exe"
                os.startfile(cam)

            elif 'send email' in query:
                try:
                    speak("What should i send ?")
                    content = takecommand()
                    to = "nirmal233103@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent successfully")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email")
            elif "open chrome" in query:
                ch = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(ch)
            elif 'open email ' in query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            elif 'thank you' in query:
                speak("welcome")
                break
            elif 'what is the time now' in query:
                v = datetime.datetime.now()
                speak(v)
            elif 'close' in query:
                speak("welcome")
                break
            elif 'open firefox' in query:
                webbrowser.open("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
            else:
                speak("I couldn't get you")


button = tkinter.Button(window,text="Click to Speak with assistant",font=100,command=clicked,bg="Yellow",width=40,height=10)

button.grid(column=5, row=0)
button.place(x=150, y=50)
window.mainloop()

