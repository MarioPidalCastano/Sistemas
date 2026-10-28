import sys
import socket

IP_POR_DEFECTO = "localhost"
PUERTO_POR_DEFECTO = 9999

MENSAJES = ["HOLA", "ADIOS", "PYTHON"]


def main():
    ip = IP_POR_DEFECTO
    if len(sys.argv) > 1:
        ip = sys.argv[1]

    puerto = PUERTO_POR_DEFECTO
    if len(sys.argv) > 2:
        puerto = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, puerto))

    for texto in MENSAJES:
        s.sendall(bytes(texto + "\r\n", "utf8"))
        respuesta = s.recv(80)
        print("Respuesta del servidor:", respuesta.decode("utf8"))

    s.close()


if __name__ == "__main__":
    main()