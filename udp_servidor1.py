import socket
import sys

puerto = 9999

if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(("", puerto))

print(f"Servidor escuchando en el puerto {puerto}")

while True:
    datos, addr = servidor.recvfrom(1024)
    mensaje = datos.decode("utf8")
    print(f"Mensaje de {addr}: {mensaje}")

    if mensaje == "FIN":
        break

servidor.close()
