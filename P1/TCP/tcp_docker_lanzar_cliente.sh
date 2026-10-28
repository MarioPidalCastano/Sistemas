#!/bin/bash
# Lanza el cliente oche (TCP) dentro de la subred "pruebas", conectando con
# el servidor por su nombre.
# Uso: ./tcp_docker_lanzar_cliente.sh
# Ejecutar desde la carpeta que contiene tcp_cliente5_oche_readline.py

docker run --rm --network pruebas -v "$(pwd)":/app \
    python:3.7 python /app/tcp_cliente5_oche_readline.py servidor_oche 9999
