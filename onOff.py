from gpiozero import Servo
from time import sleep

servo = Servo(4)

while True:
    servo.value = None
    time.sleep(10)
    servo.value = 1
    