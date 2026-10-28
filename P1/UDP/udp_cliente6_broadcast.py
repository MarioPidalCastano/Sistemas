import sys
import socket

PUERTO = 12345
TIMEOUT_DESCUBRIMIENTO = 2.0


def main():
    # IP de broadcast de la subred, p.ej. 192.168.0.255. Si no se indica,
    # se usa la de broadcast "limitado" 255.255.255.255 (solo alcanza la
    # red local directamente conectada).
    ip_broadcast = sys.argv[1] if len(sys.argv) > 1 else "255.255.255.255"

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    s.sendto("BUSCANDO HOLA".encode("utf8"), (ip_broadcast, PUERTO))

    servidores = []
    s.settimeout(TIMEOUT_DESCUBRIMIENTO)
    while True:
        try:
            datagrama, origen = s.recvfrom(1024)
            mensaje = datagrama.decode("utf8")
            if mensaje == "IMPLEMENTO HOLA":
                print(f"Servidor encontrado en {origen[0]}")
                servidores.append(origen[0])
        except socket.timeout:
            break  # Asumimos que ya no hay mas servidores respondiendo

    if not servidores:
        print("No se ha encontrado ningun servidor")
        return

    ip_servidor = servidores[0]
    print(f"Probando el servicio HOLA con {ip_servidor}...")
    s.sendto("HOLA".encode("utf8"), (ip_servidor, PUERTO))
    datagrama, origen= s.recvfrom(1024)
    print("Respuesta:", datagrama.decode("utf8"))


if __name__ == "__main__":
    main()