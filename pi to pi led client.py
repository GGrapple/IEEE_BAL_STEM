#!/usr/bin/python
'''
Author: Dan White
Client takes push button input and transmits circuit state information to server
'''
import socket
import RPi.GPIO as GPIO
import time
HOST='192.168.90.100'
PORT=3333
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
INPUTPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUTPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	if GPIO.input(INPUTPIN) == 1:
		s.send('off'.encode())
		time.sleep(.5)
	else:
		s.send('on'.encode())
		time.sleep(.5)
s.close()

