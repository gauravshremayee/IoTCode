import RPi.GPIO as GPIO

import time


#Put one pin in pin 12 and other in GND ,when the program stops LED should be off

#If the led is connected to 5v and GND pin then it will be switch on without program also.


GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(12,GPIO.OUT)

print( "LED on")

GPIO.output(12,GPIO.HIGH)

time.sleep(1)

print( "LED off")

GPIO.output(12,GPIO.LOW)

print("LED ON")

GPIO.output(12,GPIO.HIGH)