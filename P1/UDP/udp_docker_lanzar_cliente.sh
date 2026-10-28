#!/bin/bash
# Lanza el cliente HOLA (broadcast) dentro de la subred "pruebas".
# Uso: ./udp_docker_lanzar_cliente.sh [ip_broadcast]
#
# Averigua la IP de broadcast con:
#   docker inspect <nombre_contenedor> | grep -E "IPAddress|IPPrefixLen"
# Con una IP tipo 172.18.0.2 y prefijo /16, la de broadcast es 172.18.255.255

IP_BROADCAST=${1:-172.18.255.255}

docker run -it --network pruebas -v "$(pwd)":/app python:3.7 \
    python /app/udp_cliente6_broadcast.py "$IP_BROADCAST"
