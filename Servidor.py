
#Documentado por: Luis Fernando Mosquera Imbachi Codigo: 20152142148 
#
# SERVIDOR
#

import socket
import pyaudio
import sys

# UDP_IP="127.0.0.1"
UDP_IP = "192.168.0.4"#direccion local del pc que trabaja como servidor
#UDP_IP = socket.gethostname()#es El mismo codigo de arriba con este toma la up automaticamente
UDP_PORT = 80#Puerto del pc Asignado, puede ser otro

chunk = 1024 #tamaño fragmentos
FORMAT = pyaudio.paInt16#formato de audio
CHANNELS = 1# un solo canal
RATE = 8000#tasa de muestreo
RECORD_SECONDS = 1#tiempo de grabacion

#las lineas de abajo son para repetir in ciclo infinito, para que se siga grabando y trasmitiendo El audio hasta que el usuario para
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=chunk)

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)  # UDP #Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros.
sock.bind((UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(3072)
print ("received message:", data)

print ("* playing")
# for i in range(0, 44100 / chunk * RECORD_SECONDS):
#   print "get chunk %i" %i
while True:
    # data,addr = s.recvfrom(1024)
    data, addr = sock.recvfrom(3072)
    stream.write(data, chunk)
    # stream.write(data, chunk)
print ("* done")
