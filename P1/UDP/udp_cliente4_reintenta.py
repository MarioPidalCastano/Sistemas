import sys
import socket

PUERTO_POR_DEFECTO = 9999
IP_POR_DEFECTO="localhost"
TIMEOUT_MAXIMO=2
TIMEOUT_INICIAL=0.1

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
        mensaje="f{contador}:{linea}"
        recibido=comprobacion_reintento(sock=sock,linea_texto=mensaje,destinatario=(ip,puerto))
        if not recibido:
            print("No se recibe respuesta del servidor")
            break
        
        if linea_texto=="FIN":
            break
        
def comprobacion_reintento(sock,linea_texto,destinatario):
    
    timeout=TIMEOUT_INICIAL
    
    while timeout<=TIMEOUT_MAXIMO:
        sock.sendto(linea_texto.encode("utf8"),destinatario)
        sock.settimeout(timeout)
        try:
            datagrama, origen = sock.recvfrom(1024) # Tamaño máximo a recibir
            datagrama = datagrama.decode("utf8")
            if datagrama=="OK":
                print("Recibida confirmación")
                return True #Nos ha llegado la contestación del servidor
            else:
                 print("Recibido datagrama no esperado")
        except socket.timeout:
                 print("ERROR. El datagrama de confirmación no llega")
                 timeout*=2
    return False
    
    
           
if __name__ == "__main__":
    main()