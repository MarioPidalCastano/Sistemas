import sys
import socket

PUERTO_POR_DEFECTO = 9999


def recibe_mensaje(sock):
    buffer = []

    while True:
        byte = sock.recv(1)
        if byte == b"":
            break  # Conexion cerrada
        buffer.append(byte)
        if len(buffer) >= 2 and buffer[-2] + buffer[-1] == b"\r\n":
            break

    return b"".join(buffer).decode("utf8")


def main():
    puerto = PUERTO_POR_DEFECTO
    if len(sys.argv) > 1:
        puerto = int(sys.argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", puerto))
    s.listen(5)
    print(f"Servidor oche (mejorado) escuchando en el puerto {puerto}...")

    while True:
        print("Esperando un cliente")
        sd, origen = s.accept()
        print("Nuevo cliente conectado desde %s, %d" % origen)

        while True:
            mensaje = recibe_mensaje(sd)
            if mensaje == "":
                print("El cliente ha cerrado la conexion")
                break

            linea = mensaje[:-2]
            linea = linea[::-1]
            sd.sendall(bytes(linea + "\r\n", "utf8"))

        sd.close()


if __name__ == "__main__":
    main()