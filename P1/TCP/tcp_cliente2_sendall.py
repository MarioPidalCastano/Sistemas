import sys
import socket

IP_POR_DEFECTO = "localhost"
PUERTO_POR_DEFECTO = 9999


def main():
    ip = IP_POR_DEFECTO
    if len(sys.argv) > 1:
        ip = sys.argv[1]

    puerto = PUERTO_POR_DEFECTO
    if len(sys.argv) > 2:
        puerto = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, puerto))

    for i in range(5):
        s.sendall(b"ABCDE")

    s.sendall(b"FINAL")
    s.close()


if __name__ == "__main__":
    main()