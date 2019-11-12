
import RPi.GPIO as GPIO

import time

#We can use other SPIO pin also 
#Put one pin in pin 12 ( i.e BCM PIN 12)  and other in GND ,when the program stops LED should be off

#If the led is connected to 5v and GND pin then it will be switch on without program also.


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)

print( "LED on")

GPIO.output(18,GPIO.HIGH)

time.sleep(1)

print( "LED off")

GPIO.output(18,GPIO.LOW)

print("LED ON")


GPIO.output(18,GPIO.HIGH)