Conexión de un Programa.py con la tarjeta Arduino a través del puerto Serial utilizando la librería "pyserial"

import serial
ser = serial.Serial('/dev/ttyACM0', 9600) 