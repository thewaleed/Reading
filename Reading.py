from gtts import gTTS
import os

test_voice = gTTS("heloo and fuck off")

test_voice.save("thetest.mp3")

os.system("/home/kali/Desktop/Reading/thetest.mp3")

#os.remove("thetest.mp3")