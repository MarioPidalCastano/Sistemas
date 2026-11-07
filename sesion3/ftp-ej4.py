import ftplib, getpass

lista = []

def acumular(linea):
    lista.append(linea)

clave = getpass.getpass("Clave? ")

f = ftplib.FTP("localhost")
f.login("mario", clave)
f.cwd("carpeta")

f.retrlines("MLSD", acumular)

for l in lista:
    if "type=file" not in l:
        continue
    nombre = l.split(" ", 1)[1]
    f_local = open(nombre, "wb")
    f.retrbinary("RETR " + nombre, f_local.write)
    f_local.close()
    print("Descargado:", nombre)
