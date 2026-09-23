import socket
import sys

if len(sys.argv) > 2:
    puerto = int(sys.argv[1])
    ip = sys.argv[2]
else:
    puerto = 9999
    ip = "localhost"

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente arrancado")

while True:
    linea = input("> ")

    cliente.sendto(linea.encode("utf8"), (ip, puerto))

    if linea == "FIN":
        break

cliente.close()
