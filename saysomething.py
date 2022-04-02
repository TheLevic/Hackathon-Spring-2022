import gtts
from playsound import playsound

def sayThings():
    while (input != 999):
        val = input("Enter what you want him to say: ")
        tts = gtts.gTTS(val)
        sound = "say.mp3"
        tts.save(sound)
        playsound(sound)
sayThings()
    


