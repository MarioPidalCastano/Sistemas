import sys
import socket
import random

PUERTO_POR_DEFECTO = 9999


def main():
    if len(sys.argv) > 1:
        puerto=int(sys.argv[1])
    else:
        puerto=PUERTO_POR_DEFECTO

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", puerto))
    print(f"Servidor UDP escuchando en el puerto {puerto}...")

    while True:
        datagrama, origen = s.recvfrom(1024)
        aleatorio=random.randint(0,1)
        if(aleatorio==0):
            texto = datagrama.decode("utf8")
            print(f"Recibido de {origen}: {texto}")
        else:
            print(f"Simulando paquete perdido")


if __name__ == "__main__":
    main()