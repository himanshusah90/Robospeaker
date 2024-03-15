# Making a robo speaker using python

#install the pyttsx3 module in the terminal

#importing pyttsx3




import pyttsx3

engine = pyttsx3.init()

while True:
    speak = input("Enter the text to speak : ")

    if speak != 'q':
        engine.say(speak) # Making the pyttsx3 speak the text entered by the user
        engine.runAndWait()
        

    else:
        print("Thank you for using Robo Speaker !!")
        break