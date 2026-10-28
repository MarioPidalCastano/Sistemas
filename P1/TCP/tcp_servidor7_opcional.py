import sys
import socket

IP_POR_DEFECTO = "localhost"
PUERTO_POR_DEFECTO = 9999

MENSAJES = ["HOLA", "ADIOS", "PYTHON"]


def recibe_linea(sock, terminador=b"\n"):
    buffer = []
    while True:
        byte = sock.recv(1)
        if byte == b"":
            return None if not buffer else b"".join(buffer)
        if byte == terminador:
            break
        buffer.append(byte)
    return b"".join(buffer)


def recvall(sock, n):
    datos = b""
    restantes = n
    while restantes > 0:
        fragmento = sock.recv(restantes)
        if fragmento == b"":
            break
        datos += fragmento
        restantes -= len(fragmento)
    return datos


def enviar_mensaje(sock, texto):
    datos = bytes(texto, "utf8")
    cabecera = ("%d\n" % len(datos)).encode("ascii")
    sock.sendall(cabecera + datos)


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
        enviar_mensaje(s, texto)

        linea_longitud = recibe_linea(s, b"\n")
        longitud = int(linea_longitud.decode("ascii"))
        respuesta = recvall(s, longitud).decode("utf8")
        print("Respuesta:", respuesta)

    s.close()


if __name__ == "__main__":
    main()