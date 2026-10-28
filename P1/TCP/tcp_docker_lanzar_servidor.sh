#!/bin/bash
# Lanza el servidor oche (TCP) en la subred "pruebas", publicando su puerto
# hacia el anfitrion.
# Uso: ./tcp_docker_lanzar_servidor.sh [puerto_anfitrion]
# Ejecutar desde la carpeta que contiene tcp_servidor5_oche_readline.py

PUERTO_ANFITRION=${1:-9090}
PUERTO_CONTENEDOR=9999

docker network create pruebas 2>/dev/null || true

docker run -d --rm -p "${PUERTO_ANFITRION}:${PUERTO_CONTENEDOR}" \
    --network pruebas --name servidor_oche -v "$(pwd)":/app \
    python:3.7 python /app/tcp_servidor5_oche_readline.py

echo "Servidor lanzado. Puerto del anfitrion: ${PUERTO_ANFITRION}"
docker ps
