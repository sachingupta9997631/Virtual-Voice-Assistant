import speech_recognition as sr
import pyautogui as pg
import os
import pyttsx3
import wikipedia as wiki

r=sr.Recognizer()
loud = pyttsx3.init()
#for the voice of a female
voices = loud.getProperty('voices')
loud.setProperty('voice',voices[1].id)

loud.say("Waiting for your wakeup keyword...")
loud.runAndWait()

while True:
    with sr.Microphone() as source:
        try:
            audio=r.listen(source)
            text=r.recognize_google(audio,language='eng-in')
            text=text.split()
            if "start" in text:
                loud.say("Ready to Listen for Your Commands")
                loud.runAndWait()
                break
            else:
                pass
        except:
            pass

def loud_voice(a):
    global loud
    loud.say(str(a))
    loud.runAndWait()

def recog(command):
    command=command.split()

    strt = ['hey', 'hello', 'hey there', 'namaste', 'hey buddy']
    if command[0] in strt:
        print_txt="Hi Developer... i am your Virtual Assistant here... how can i help you?"
        loud_voice(print_txt)
        print(print_txt)
        return 0
    
    if "Mouse" in command and "position" in command:
        print("Mouse Position is at: {}".format(pg.position()))
        "Mouse Position is at: {}".format(pg.position())
        loud_voice(str("Mouse Position is at: {}".format(pg.position())))
        return 0

    if "wikipedia" in command or "search" in command:
        print_txt="Say the Topic Name for the Search: "
        loud_voice(print_txt)
        print(print_txt)
        try:
            with sr.Microphone() as source:
                audio=r.listen(source)
            data=r.recognize_google(audio,language='eng-in')
            reslt = wiki.summary(str(data), sentences = 2)
            print_txt = "the result is: {}".format(reslt)
            print(print_txt)
            loud_voice(print_txt)
        except:
            print_txt = "Oops! an error occured while recognizing your voice"
            loud_voice(print_txt)
            print("Oops! an error occurred...")
        
        return 0
    
    #if "recognition" in command or "recognize":
    #    try:
    #        with sr.Microphone() as source:
    #            audio=r.listen(source)
    #        data=r.recognize_google(audio,language='eng-in')
    #        pg.typewrite(data)
    #    except:
    #        print_txt = "Oops! an error occured while recognizing your voice"
    #        loud_voice(print_txt)
    #        print("Oops! an error occurred...")
    #    return 0
            
    if "copy" in command and "up" in command:
        print_txt = "the data has been copied"
        loud_voice(print_txt)
        pg.hotkey("ctrlleft","a")   #control button + a
        pg.hotkey("ctrlleft","c")
        return 0

    if "copy" in command and "down" in command:
        print_txt = "the data has been pasted"
        loud_voice(print_txt)
        pg.hotkey("ctrlleft","v")
        return 0

    if "undo" in command:
        print_txt = "command undo is executed"
        loud_voice(print_txt)
        pg.hotkey("ctrlleft","z")
        return 0
    
    if "redo" in command:
        print_txt = "command redo is executed"
        loud_voice(print_txt)
        pg.hotkey("ctrlleft","y")
        return 0
    
    if "volume" in command and "up" in command:
        print_txt = "volume has been increased"
        loud_voice(print_txt)
        pg.press("up")
        return 0

    if "volume" in command and "down" in command:
        print_txt = "volume has been decreased"
        loud_voice(print_txt)
        pg.press("down")
        return 0

    if "play" in command or "pause" in command:
        pg.press("space")
        return 0
    
    if "exit" in command:
        exit()
    
    if "what's up" == command or "what's going on" == command:
        print_txt = "Nothing Very Special...You say!"
        print(print_txt)
        loud_voice(print_txt)
        return 0

    if "i'm fine" in command or "good" in command or "fine" in command:
        print_txt = "Good!"
        loud_voice(print_txt)
        print(print_txt)
        return 0
    
    if "shut" in command and "down" in command:
        print_txt = "shutting down the system withing few seconds"
        loud_voice(print_txt)
        os.system("shutdown -s -t 5")
        return 0

    if "log" == command[0] and "off" == command or command[0]=="log":
        print_txt = "logging off the system"
        loud_voice(print_txt)
        os.system("shutdown -l")
        return 0

    if "camera" in command:
        print_txt = "Starting with microsoft camera"
        loud_voice(print_txt)
        os.system("start microsoft.windows.camera")
        return 0

    if "share" in command and "data" in command:
        print_txt = "just get lost and forget about this idea"
        print("Just get Lost...")
        loud_voice(print_txt)
        return 0

    if "notepad" in command or "Notepad" in command:
        print_txt = "opening Notepad"
        loud_voice(print_txt)
        os.system("notepad")
        return 0

    if ("command" in command or "Prompt" in command) or "CMD" in command:
        print_txt = "Opening Microsoft Command Prompt"
        loud_voice(print_txt)
        os.system("cmd")
        return 0

    if "ms paint" in command or "paint" in command or "MS paint" in command:
        print_txt = "Opening Microsoft Paint"
        loud_voice(print_txt)
        os.system("mspaint")
        return 0

    if "joke" in command:
        print_txt = "go and watch your face in the mirror"
        loud_voice(print_txt)
        print("go and watch your face in the mirror")
        return 0

    if "make" in command and "note" in command:
        file = open("note1.txt","w")
        print_txt = "say something to note down"
        loud_voice(print_txt)
        print("Say Something to note down: ")
        try:
            with sr.Microphone() as source:
                audio=r.listen(source)
            data=r.recognize_google(audio,language='eng-in')
            file.write(str(data))
            print_txt = "the data was recorded to the file"
            loud_voice(print_txt)
            print(print_txt)
            file.close()
        except:
            print_txt = "Error in writing to the file"
            print("Error in writing to the file")
            loud_voice(print_txt)
        return 0


print("say")
while True:
    with sr.Microphone() as source:
        try:
            #print("Speak Anything: ")
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio,language='eng-in')
                print("You: ",text)
                recog(text)
            except:
                pass
        except:
            print("Sorry we could not recognize your voice")
        
