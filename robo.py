#import the modules
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

#creating listener
r = sr.Recognizer()

#initialize
machine = pyttsx3.init()

#creating a function and passing parameter that we want to hear
def talk(text):
     machine.say(text)
     machine.runAndWait()

#function for instruction as input
def get_instruction():
    try:
       with sr.Microphone(device_index=0) as source:
          print("Listening...")
          r.adjust_for_ambient_noise(source)
          speech = r.listen(source)

          # using google API to convert to text
          instruction = r.recognize_google(speech)
          instruction = instruction.lower()

          #detect robo
          if "robo" in instruction:
             instruction = instruction.replace('robo', "")
             
             return instruction
          
    except Exception as e:
        print("An error occurred: {e}")

    return instruction

#function for performing tasks
def play_Robo():
    instruction = get_instruction()
    print(instruction) 

    #to play on youtube   
    if "play" in instruction:
       song = instruction.replace('play', "") 
       talk("Playing " + song)   
       pywhatkit.playonyt(song)
       
    #to know time
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
        print("The current time is " + time)

    #to know date
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's Date" + date)
        print("Today's date is " + date)

    #to recognize basic greet
    elif 'how are you' in instruction:
         talk("I am fine, How about you?")
         print("I am fine, How about you?")

    elif 'what is your name' in instruction:
        talk("I am Robo, What can I do for you?")
        print("I am Robo, What can I do for you?")

    #to get information from wikipedia
    elif 'who is' in instruction:
        command = instruction.replace("who is", " ")
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)

    #if it doesn't hear
    else:
        talk("I didn't get you. Please repeat.")
        print("I didn't get you. Please repeat.")
  
play_Robo()