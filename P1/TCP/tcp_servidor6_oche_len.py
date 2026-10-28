import sys
import socket

PUERTO_POR_DEFECTO = 9999


def recibe_linea(sock, terminador=b"\n"):
    """Lee bytes de uno en uno del socket hasta encontrar el terminador (que
    NO se incluye en el resultado). Devuelve None si el cliente cierra la
    conexion antes de enviar nada."""
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
    """Recibe exactamente n bytes del socket."""
    datos = b""
    restantes = n
    while restantes > 0:
        fragmento = sock.recv(restantes)
        if fragmento == b"":
            break
        datos += fragmento
        restantes -= len(fragmento)
    return datos


def main():
    puerto = PUERTO_POR_DEFECTO
    if len(sys.argv) > 1:
        puerto = int(sys.argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", puerto))
    s.listen(5)
    print(f"Servidor oche (longitud en ASCII) escuchando en el puerto {puerto}...")

    while True:
        print("Esperando un cliente")
        sd, origen = s.accept()
        print("Nuevo cliente conectado desde %s, %d" % origen)

        while True:
            # Primero leemos, byte a byte, la linea con la longitud
            linea_longitud = recibe_linea(sd, b"\n")
            if linea_longitud is None:
                print("El cliente ha cerrado la conexion")
                break

            longitud = int(linea_longitud.decode("ascii"))
            # Ahora ya sabemos cuantos bytes pedir para el mensaje en si
            mensaje = recvall(sd, longitud).decode("utf8")
            linea = mensaje[::-1]

            datos_linea = bytes(linea, "utf8")
            cabecera = ("%d\n" % len(datos_linea)).encode("ascii")
            sd.sendall(cabecera + datos_linea)

        sd.close()


if __name__ == "__main__":
    main()