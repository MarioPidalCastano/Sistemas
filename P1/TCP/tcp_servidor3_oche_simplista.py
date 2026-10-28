import sys
import socket

PUERTO_POR_DEFECTO = 9999


def main():
    puerto = PUERTO_POR_DEFECTO
    if len(sys.argv) > 1:
        puerto = int(sys.argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", puerto))
    s.listen(5)
    print(f"Servidor oche (simplista) escuchando en el puerto {puerto}...")

    while True:
        print("Esperando un cliente")
        sd, origen = s.accept()
        print("Nuevo cliente conectado desde %s, %d" % origen)

        while True:
            # Suposicion: cada recv() trae una linea completa terminada en \r\n
            mensaje = sd.recv(80)
            if mensaje == b"":
                print("El cliente ha cerrado la conexion")
                break

            mensaje = str(mensaje, "utf8")
            linea = mensaje[:-2]   # Quitamos el \r\n final
            linea = linea[::-1]    # Le damos la vuelta

            sd.sendall(bytes(linea + "\r\n", "utf8"))

        sd.close()


if __name__ == "__main__":
    main()