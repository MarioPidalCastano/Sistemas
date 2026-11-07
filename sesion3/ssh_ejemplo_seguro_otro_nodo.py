import paramiko
import time
import getpass
import base64
client = paramiko.SSHClient()
key = paramiko.Ed25519Key(data=base64.b64decode(b' AAAAC3NzaC1lZDI1NTE5AAAAIKBahgzh2lKodQlP6OeyoYCSFm2Aj+/9TL+YDCmQU9Jr'))
client.get_host_keys().add('192.168.1.28', 'ssh-ed25519', key)
clave = getpass.getpass("Clave? ")
client.connect('192.168.1.28', username='mario', password=clave)
print("Conectado!!")

# Ejecutar comando remoto, redireccionando sus salidas
stdin, stdout, stderr = client.exec_command('ls')

# Mostrar resultado de la ejecución (rstrip quita los retornos de carro)
for line in stdout:
    print(line.rstrip())
time.sleep(1)  # Dar tiempo a que se vacie el buffer
client.close()
