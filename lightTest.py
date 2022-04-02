
#!/usr/bin/env python3

# file: light_meter.py
from gpiozero import LED
import picamera 
import picamera.array 
import numpy as np
from time import sleep
from playsound import playsound
import time
import random

def playSound():
        i = random.randrange(0, 22)
        n = str(i) + ".mp3"
        playsound(n)
        time.sleep(8)


def main():
	led = LED(26)
	with picamera.PiCamera() as camera:
		camera.resolution = (320, 240) 
		with picamera.array.PiRGBArray(camera) as stream:
			camera.exposure_mode = 'auto' 
			camera.awb_mode = 'auto' 
			print("Initializing Pi Camera") 
			sleep(2) 
			camera.exposure_mode = 'off' 
			while True:
				try:
					camera.capture(stream, format='rgb')
					# pixAverage = int(np.average(stream.array[...,1]))
					pixAverage = np.average(stream.array[...,1]) 
					print ("Light Meter pixAverage: {:.1f}".format(pixAverage)) 
					sleep(1) 
					stream.truncate() 
					stream.seek(0)
				except KeyboardInterrupt:
					print("\nExiting ..") 
					break
				if(pixAverage < 40):
					print("dark room homie")
					led.on()
					playSound()					
				if(pixAverage > 40):
					print("its lighter than ryan")
					led.off()


if __name__ == "__main__": main()



