import sys
import socket

IP_POR_DEFECTO = "localhost"
PUERTO_POR_DEFECTO = 9999

MENSAJES = ["UNO", "DOS", "TRES"]


def main():
    ip = IP_POR_DEFECTO
    if len(sys.argv) > 1:
        ip = sys.argv[1]

    puerto = PUERTO_POR_DEFECTO
    if len(sys.argv) > 2:
        puerto = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, puerto))

    # Primero se envian los tres mensajes seguidos, sin esperar respuesta
    for texto in MENSAJES:
        s.sendall(bytes(texto + "\r\n", "utf8"))

    # Despues se intentan leer las tres respuestas
    for i in MENSAJES:
        respuesta = s.recv(80)
        respuesta = respuesta.decode("utf8")
        print(repr(respuesta))

    s.close()


if __name__ == "__main__":
    main()