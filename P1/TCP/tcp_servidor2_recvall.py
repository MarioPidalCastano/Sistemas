import sys
import socket

PUERTO_POR_DEFECTO = 9999


def recvall(sock, n):
    datos = b""
    restantes = n
    while restantes > 0:
        fragmento = sock.recv(restantes)  # Pedimos de una vez lo que falta
        if fragmento == b"":
            break  # El otro extremo cerro la conexion
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
    print(f"Servidor TCP (con recvall) escuchando en el puerto {puerto}...")

    while True:
        print("Esperando un cliente")
        sd, origen = s.accept()
        print("Nuevo cliente conectado desde %s, %d" % origen)

        continuar = True
        while continuar:
            datos = recvall(sd, 5)
            datos = datos.decode("ascii")

            if datos == "":
                print("Conexion cerrada de forma inesperada por el cliente")
                sd.close()
                continuar = False
            elif datos == "FINAL":
                print("Recibido mensaje de finalizacion")
                sd.close()
                continuar = False
            else:
                print("Recibido mensaje: %s" % datos)


if __name__ == "__main__":
    main()