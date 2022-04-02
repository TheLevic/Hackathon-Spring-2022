from gpiozero import LED
from time import sleep

led = LED(26)

while True:
	led.off()
	sleep(5)
	led.on()
	sleep(5)
