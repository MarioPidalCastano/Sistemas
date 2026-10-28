import sys
import socket
import uuid

IP_POR_DEFECTO = "localhost"
PUERTO_POR_DEFECTO = 9999
TIMEOUT_INICIAL = 0.5
TIMEOUT_MAXIMO = 2.0

def main():
    ip = IP_POR_DEFECTO
    puerto = PUERTO_POR_DEFECTO
    
    if len(sys.argv) > 1:
        ip=sys.argv[1]

    if len(sys.argv) > 2:
        puerto=int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # En UDP, connect() no crea conexion real: solo fija con quien se habla,
    # de modo que recv() descartara datagramas que no vengan de ese origen.
    s.connect((ip, puerto))

    while True:
        linea = input("Escribe un mensaje (FIN para salir): ")
        exito = enviar_con_reintentos(s, linea)
        if not exito:
            print("Puede que el servidor este caido. Intentelo mas tarde")
            break
        if linea == "FIN":
            break



def enviar_con_reintentos(s, texto):
    # Identificador aleatorio: el mismo se reutiliza en todos los reintentos
    # de este mensaje, para que el servidor pueda detectar duplicados y para
    # que el cliente sepa a que mensaje corresponde cada confirmacion.
    id_msg = uuid.uuid4().hex[:8]
    mensaje = f"{id_msg}:{texto}"
    timeout = TIMEOUT_INICIAL

    while timeout <= TIMEOUT_MAXIMO:
        s.send(mensaje.encode("utf8"))  # connect() ya fijo el destino
        s.settimeout(timeout)
        try:
            datagrama = s.recv(1024)  # recv() descarta lo que no venga del servidor
            respuesta = datagrama.decode("utf8")
            tipo, separador, id_confirmado = respuesta.partition(":")
            if tipo == "OK" and id_confirmado == id_msg:
                print(f"Recibida confirmacion para el mensaje {id_msg}")
                return True
            else:
                print("Recibida una confirmacion inesperada; se ignora")
        except socket.timeout:
            print(f"ERROR. El datagrama de confirmacion no llega (timeout={timeout}s)")
            timeout *= 2

    return False

if __name__ == "__main__":
    main()