import sys
import socket

PUERTO_POR_DEFECTO = 9999


def main():
    puerto = PUERTO_POR_DEFECTO
    if len(sys.argv) > 1:
        puerto = int(sys.argv[1])

    # Creacion del socket de escucha
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", puerto))
    s.listen(5)  # Maximo de clientes en la cola de espera al accept()
    print(f"Servidor TCP escuchando en el puerto {puerto}...")

    # Bucle principal de espera por clientes
    while True:
        print("Esperando un cliente")
        sd, origen = s.accept()
        print("Nuevo cliente conectado desde %s, %d" % origen)

        continuar = True
        # Bucle de atencion al cliente conectado
        while continuar:
            datos = sd.recv(5)  # Observar que se lee del socket sd, no de s
            datos = datos.decode("ascii")  # Pasar los bytes a caracteres

            if datos == "":  # Si no se reciben datos, el cliente cerro el socket
                print("Conexion cerrada de forma inesperada por el cliente")
                sd.close()
                continuar = False
            elif datos == "FINAL":
                print("Recibido mensaje de finalizacion")
                sd.close()
                continuar = False
            else:
                print("Recibido mensaje: %s" % datos)


if __name__ == "__main__":
    main()