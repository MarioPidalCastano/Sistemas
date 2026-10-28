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
    print(f"Servidor oche (readline) escuchando en el puerto {puerto}...")

    while True:
        print("Esperando un cliente")
        sd, origen = s.accept()
        print("Nuevo cliente conectado desde %s, %d" % origen)

        # "Convertimos" el socket en fichero para poder usar readline()
        f = sd.makefile(encoding="utf8", newline="\r\n")

        while True:
            mensaje = f.readline()
            if mensaje == "":
                print("El cliente ha cerrado la conexion")
                break

            linea = mensaje[:-2]
            linea = linea[::-1]
            sd.sendall(bytes(linea + "\r\n", "utf8"))

        sd.close()


if __name__ == "__main__":
    main()