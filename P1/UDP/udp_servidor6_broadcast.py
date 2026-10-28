import socket

PUERTO = 12345


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(("", PUERTO))
    print(f"Servidor HOLA escuchando en el puerto {PUERTO}...")

    while True:
        datagrama, origen = s.recvfrom(1024)
        mensaje = datagrama.decode("utf8")
        ip_cliente = origen[0]

        if mensaje == "BUSCANDO HOLA":
            print(f"Descubrimiento recibido de {origen}")
            s.sendto("IMPLEMENTO HOLA".encode("utf8"), origen)
        elif mensaje == "HOLA":
            print(f"Peticion HOLA de {origen}")
            respuesta = f"HOLA: {ip_cliente}"
            s.sendto(respuesta.encode("utf8"), origen)
        else:
            print(f"Mensaje no reconocido de {origen}: {mensaje}")


if __name__ == "__main__":
    main()