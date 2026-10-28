#!/bin/bash
# Lanza tres servidores HOLA (broadcast) en la subred "pruebas".
# Uso: ./udp_docker_lanzar_servidores.sh
# Ejecutar desde la carpeta que contiene udp_servidor6_broadcast.py

set -e

docker network create pruebas 2>/dev/null || true

for i in 1 2 3; do
    docker run -d --name "servidor_hola_$i" --network pruebas \
        -v "$(pwd)":/app python:3.7 python /app/udp_servidor6_broadcast.py
done

echo "Servidores lanzados:"
docker ps
