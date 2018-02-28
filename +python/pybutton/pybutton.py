

import serial
 

#ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)	# Conexion
ser = serial.Serial('/dev/ttyACM0', 9600)
print "conectado"

value = ser.readline()
print "recibido"
print '\nValor retornado de Arduino: %s' % (value)
 

arduinoPort.close()