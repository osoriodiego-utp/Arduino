# Python 2 - Tk inter (ttk) - PySerial (Arduino)
# GUI encendido y apagado LEd conectado a Arduino
# by Nano Osorio (dieferosorio@utp.edu.co)
#---------------------------------------------------

import sys

import Tkinter as tk
import ttk

import serial
ser = serial.Serial('/dev/ttyACM0', 9600) 


control = tk.Tk()
#control.title('')
#control.geometry('000x000')
control.configure(bg='black')

def call_on():
    print ("Pressed ON ")
    ser.write('e')

def call_off():
    print ("Pressed OFF ")
    ser.write('a')

def call_exit():
	print ("Pressed EXIT ")
	sys.exit()

boton1 = ttk.Button(control, text="ON", command=call_on)
boton2 = ttk.Button(control, text="OFF", command=call_off)
boton3 = ttk.Button(control, text=" SALIR ", command=call_exit)

boton1.pack()
boton2.pack()
boton3.pack()

control.mainloop()