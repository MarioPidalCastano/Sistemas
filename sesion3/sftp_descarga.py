import paramiko
import time
import getpass
import base64
from stat import S_ISDIR
client = paramiko.SSHClient()
key = paramiko.Ed25519Key(data=base64.b64decode(b' AAAAC3NzaC1lZDI1NTE5AAAAIKBahgzh2lKodQlP6OeyoYCSFm2Aj+/9TL+YDCmQU9Jr'))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)
clave = getpass.getpass("Clave? ")
client.connect('localhost', username='mario', password=clave)
print("Conectado!!")

sftp = client.open_sftp()

carpeta = input("Carpeta remota: ")
sftp.chdir(carpeta)
listado = sftp.listdir()
for nombre in listado:
    # para saber si es un directorio:
    if S_ISDIR(sftp.stat(nombre).st_mode):
        continue
    sftp.get(nombre, "descargas/" + nombre)
    print("Descargado:", nombre)

client.close()
