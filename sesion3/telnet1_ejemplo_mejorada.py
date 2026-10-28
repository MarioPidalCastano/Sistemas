import telnetlib
import getpass

HOST = "localhost"

user = input("Introduce tu nombre de usuario: ")
password = getpass.getpass("Introduce tu contraseña: ")


tn = telnetlib.Telnet(HOST)


tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")


tn.read_until(b"Password: ")
tn.write(password.encode('utf-8') + b"\n")

tn.read_until(b"$")


tn.write(b"ls /home\n")
tn.write(b"exit\n")


salida = tn.read_all().decode('utf-8')
print(salida)
