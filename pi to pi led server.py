#! /usr/bin/python
'''
Author: Dan White
Server takes received push button input and activates LED
'''
import RPi.GPIO as GPIO
import socket
import time
HOST='0.0.0.0'
PORT=3333
YELLOWLED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(YELLOWLED, GPIO.OUT)
GPIO.output(YELLOWLED, 0)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('Server started on port: ', PORT)
s.listen(1)
conn, addr=s.accept()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
print 'Connected by', addr
data=conn.recv(1024)
while True:
	if data=='on':
                print 'Yellow LED ON'
                GPIO.output(YELLOWLED,1)
        elif data=='off':
                print 'Yellow LED OFF'
                GPIO.output(YELLOWLED, 0)
s.close()


