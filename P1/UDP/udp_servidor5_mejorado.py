import sys
import socket
import random

PUERTO_POR_DEFECTO = 9999


def main():
    if len(sys.argv) > 1:
        puerto=int(sys.argv[1])
    else:
        puerto=PUERTO_POR_DEFECTO


    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", puerto))
    print(f"Servidor UDP mejorado escuchando en el puerto {puerto}...")

    # Guardamos los identificadores ya procesados para no repetir la accion
    # asociada si llega un reenvio duplicado del mismo datagrama.
    ids_procesados = set()

    while True:
        datagrama, origen = s.recvfrom(1024)

        if random.randint(0, 1) == 0:
            print("Simulando paquete perdido")
            continue

        mensaje = datagrama.decode("utf8")
        # Formato esperado: "id:texto"
        id_msg,separador, texto = mensaje.partition(":")

        if id_msg in ids_procesados:
            print(f"Datagrama duplicado (id={id_msg}); se reenvia OK sin reprocesar")
        else:
            ids_procesados.add(id_msg)
            print(f"Recibido de {origen}: {texto}")

        confirmacion = f"OK:{id_msg}"
        s.sendto(confirmacion.encode("utf8"), origen)


if __name__ == "__main__":
    main()