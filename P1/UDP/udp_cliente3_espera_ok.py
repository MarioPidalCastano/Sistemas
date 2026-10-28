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
    contador=0
    
    while True:
        linea_texto=input("Escribe un mensaje(FIN para salir)")
        contador=contador+1
        mensaje=f"{contador:}+{linea_texto}"
        sock.sendto(mensaje.encode("utf8"),(ip,puerto))
        
        sock.settimeout(1.0)
        try:
            datagrama, origen = sock.recvfrom(1024) # Tamaño máximo a recibir
            datagrama = datagrama.decode("utf8")
            if datagrama=="OK":
                print("Recibida confirmación")
            else:
                 print("Recibido datagrama no esperado")
        except socket.timeout:
                 print("ERROR. El datagrama de confirmación no llega")
        if linea_texto=="FIN":
            break
           
if __name__ == "__main__":
    main()