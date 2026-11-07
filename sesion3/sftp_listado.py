import paramiko
import time
import getpass
import base64
client = paramiko.SSHClient()
key = paramiko.Ed25519Key(data=base64.b64decode(b' AAAAC3NzaC1lZDI1NTE5AAAAIKBahgzh2lKodQlP6OeyoYCSFm2Aj+/9TL+YDCmQU9Jr'))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)
clave = getpass.getpass("Clave? ")
client.connect('localhost', username='mario', password=clave)
print("Conectado!!")

# Ejecutar comando remoto, redireccionando sus salidas
sftp = client.open_sftp()

listado = sftp.listdir()

# Mostrar resultado de la ejecución (rstrip quita los retornos de carro)
listado = sftp.listdir()
for nombre in listado:
    print(nombre)

client.close()
