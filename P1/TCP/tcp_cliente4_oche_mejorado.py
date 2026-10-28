import sys
import socket

IP_POR_DEFECTO = "localhost"
PUERTO_POR_DEFECTO = 9999

MENSAJES = ["UNO", "DOS", "TRES"]


def recibe_mensaje(sock):
    buffer = []

    while True:
        byte = sock.recv(1)
        if byte == b"":
            break
        buffer.append(byte)
        if len(buffer) >= 2 and buffer[-2] + buffer[-1] == b"\r\n":
            break

    return b"".join(buffer).decode("utf8")


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

    for _ in MENSAJES:
        respuesta = recibe_mensaje(s)
        print(repr(respuesta))

    s.close()


if __name__ == "__main__":
    main()