from time import sleep
from playsound import playsound
import time

def playSound():
    for i in range(1, 23):
        n = str(i) + ".mp3"
        playsound(n)
        time.sleep(8)
    
playSound()