
import telnetlib
import time


HOST = "127.0.0.1"  # IP de la máquina Ubuntu
USUARIO = "mario"
CLAVE = "Mario21080251S."

def main():
    # 1. Conectar por Telnet e iniciar sesión
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"login: ")
    tn.write(USUARIO.encode("utf-8") + b"\n")

    tn.read_until(b"Password: ")
    tn.write(CLAVE.encode("utf-8") + b"\n")

    # 2. Esperar al prompt del shell
    tn.read_until(b"$")

    # 3. Pedir la lista de procesos
    tn.write(b"ps -ef\n")

    # 4. Leer la respuesta hasta el siguiente prompt
    respuesta = tn.read_until(b"$")

    # 5. Comprobar si el servidor ya está ejecutándose
    if b"udp_servidor3_con_ok.py" in respuesta:
        print("El servidor ya está en ejecución")

    else:
        # 6. Lanzar el servidor en segundo plano
        tn.write(
            b"nohup python3 udp_servidor3_con_ok.py &\n"
        )

        # 7. Dar tiempo al servidor para arrancar
        time.sleep(1)

    # 8. Cerrar el shell remoto
    tn.write(b"exit\n")

    # 9. Recoger y mostrar la respuesta final
    respuesta_final = tn.read_all()
    print(respuesta_final.decode("utf-8", errors="replace"))


if __name__ == "__main__":
    main()

