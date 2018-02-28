import sys
import subprocess

import serial
ser = serial.Serial('/dev/ttyACM0', 9600) 

while (True):
	value= ser.read()
	print (value)