
#Documentado por: Luis Fernando Mosquera Imbachi Codigo: 20152142148
#
#    CLIENTE
#
import socket
import pyaudio
import sys

# UDP_IP="127.0.0.1"
UDP_IP = "186.80.43.136"#direccion ip publica para conectar al servidor
#UDP_IP = socket.gethostname()#es El mismo codigo de arriba con este toma la up automaticamente

UDP_PORT = 80#Puerto del pc Asignado, puede ser otro
MESSAGE = "Hello, World!".encode() #mensaje que se envia Al servidor

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
#los tres print de arriba son para enviar El mensaje por protocolo de trasporte udp

chunk = 1024 #tamaño fragmentos
FORMAT = pyaudio.paInt16 #formato de audio
CHANNELS = 1 # un solo canal
RATE = 8000 #tasa de muestreo
RECORD_SECONDS = 1 #tiempo de grabacion

#las lineas de abajo son para repetir in ciclo infinito, para que se siga grabando y trasmitiendo El audio hasta que el usuario para
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=chunk)

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)  #UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) #envia un mensaje a la direccion Ip especificada

print ("* recording")
# for i in range(0, 44100 / chunk * RECORD_SECONDS):
while True:
    MESSAGE = stream.read(chunk) #realiza la lectura del mensaje transmitido por partes
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # internet # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))# envia el audio a la IP especificada
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

print ("* done")
