# Python 2 - Tk inter (ttk) - PySerial (Arduino)
# GUI conversion y envio de clave morse desde entrada de texto
# by Nano Osorio (dieferosorio@utp.edu.co)
#---------------------------------------------------

import Tkinter as tk
import ttk

import sys
import subprocess

import serial
ser = serial.Serial('/dev/ttyACM0', 9600) 

vent= tk.Tk()
vent.title(' MORSE 0.2 ')


c_label = tk.Label(vent,text="Texto: ")
#c_label.pack()
c_label.grid(row=1,column=1)

c_texto= tk.Entry(vent)
c_texto.grid(row=1,column=1)
#c_texto.pack()

'''
def obtener():
	value= c_texto.get()
	print(value)
	for ch in value:
		ser.write(ch)
		print(morse_ch(ch))
	print
'''

def get_send():
	value=c_texto.get()
	subprocess.call("clear")
	print(value)
	for ch in value:
		clave= morse_ch(ch)
		for cod in clave:
			ser.write(cod)
		ser.write(' ')
		print (clave)
	print

def f_SOS():
	value="SOS"
	subprocess.call("clear")
	print(value)
	for ch in value:
		clave= morse_ch(ch)
		for cod in clave:
			ser.write(cod)
		ser.write(' ')
		print (clave)
	print

def f_delete():
	c_texto.delete(0, tk.END)

def morse_ch(caracter):
	codigo= ''
	if caracter == 'a' or caracter == 'A':
		codigo='.-'
	if caracter == 'b' or caracter == 'B':
		codigo = '-...'
	if caracter == 'c' or caracter == 'C':
		codigo = '-.-.'
	if caracter == 'd' or caracter == 'D':
		codigo = '-..'
	if caracter == 'e' or caracter == 'E':
		codigo = '.'
	if caracter == 'f' or caracter == 'F':
		codigo = '..-.'
	if caracter == 'g' or caracter == 'G':
		codigo = '--.'
	if caracter == 'h' or caracter == 'H':
		codigo = '....'
	if caracter == 'i' or caracter == 'I':
		codigo = '..'
	if caracter == 'j' or caracter == 'J':
		codigo = '.---'
	if caracter == 'k' or caracter == 'K':
		codigo = '-.-'
	if caracter == 'l' or caracter == 'L':
		codigo = '.-..'
	if caracter == 'm' or caracter == 'M':
		codigo = '--'
	if caracter == 'n' or caracter == 'N':
		codigo = '-.'
	if caracter == 'o' or caracter == 'O':
		codigo = '---'
	if caracter == 'p' or caracter == 'P':
		codigo = '.--.'
	if caracter == 'q' or caracter == 'Q':
		codigo = '--.-'
	if caracter == 'r' or caracter == 'R':
		codigo = '.-.'
	if caracter == 's' or caracter == 'S':
		codigo = '...'
	if caracter == 't' or caracter == 'T':
		codigo = '_'
	if caracter == 'u' or caracter == 'U':
		codigo = '..-'
	if caracter == 'v' or caracter == 'V':
		codigo = '...-'
	if caracter == 'w' or caracter == 'W':
		codigo = '.--'
	if caracter == 'x' or caracter == 'X':
		codigo = '-..-'
	if caracter == 'y' or caracter == 'Y':
		codigo = '-.--'
	if caracter == 'z' or caracter == 'Z':
		codigo = '--..'
	if caracter == '0':
		codigo = '-----'
	if caracter == '1':
		codigo = '.----'
	if caracter == '2':
		codigo = '..---'
	if caracter == '3':
		codigo = '...--'
	if caracter == '4':
		codigo = '....-'
	if caracter == '5':
		codigo = '.....'
	if caracter == '6':
		codigo = '-....'
	if caracter == '7':
		codigo = '--...'
	if caracter == '8':
		codigo = '---..'
	if caracter == '9':
		codigo = '----.'
	if caracter == '.':
		codigo = '.-.-.-'
	if caracter == ',':
		codigo = '--..--'
	if caracter == '?':
		codigo = '..--..'
	if caracter == '!':
		codigo = '-.-.--'
	if caracter == ' ':
		codigo = ' '
	return codigo

def morse_w(*entrada):
	cadena= ''
	for ch in entrada:
		cadena += ch
		#cadena += morse_ch(ch)
	return cadena


b_send= ttk.Button(vent, text='SEND', command= get_send)
#b_send.pack()
b_send.grid(row=2,column=1)

b_SOS= ttk.Button(vent, text='SOS', command= f_SOS)
#b_SOS.pack()
b_SOS.grid(row=2,column=2)

b_delete= ttk.Button(vent, text='CLEAR', command= f_delete)
#b_delete.pack()
b_delete.grid(row=2,column=3)

b_exit= ttk.Button(vent, text='EXIT', command=quit)
#b_exit.pack()
b_exit.grid(row=2,column=4)



vent.mainloop()


