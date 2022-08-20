import pyttsx3

speach = pyttsx3.init()
text = "helooll motha fokos"
speach.say(text)
speach.runAndWait()