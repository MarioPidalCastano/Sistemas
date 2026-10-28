import sys
import socket

PUERTO_POR_DEFECTO = 9999
IP_POR_DEFECTO="localhost"

def main():
    ip = IP_POR_DEFECTO
    puerto = PUERTO_POR_DEFECTO
    
    if len(sys.argv) > 1:
        ip=sys.argv[1]

    if len(sys.argv) > 2:
        puerto=int(sys.argv[2])

    
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    while True:
        linea_texto=input("Escribe un mensaje(FIN para salir)")
        if(linea_texto=="FIN"):
            break
        sock.sendto(linea_texto.encode("utf8"),(ip,puerto))

if __name__ == "__main__":
    main()
