#!/bin/bash

# Duración máxima en segundos (3 minutos = 180 segundos)
DURATION=180
# Intervalo de ejecución en segundos (cada 5 segundos)
INTERVAL=5
# Contador inicial
ELAPSED=0

# Bucle para ejecutar el script cada 5 segundos durante 3 minutos
while [ $ELAPSED -lt $DURATION ]; do
    # Ejecutar el programa viewDb.py
    python3 viewDb.py

    # Esperar 5 segundos
    sleep $INTERVAL

    # Incrementar el tiempo transcurrido
    ELAPSED=$((ELAPSED + INTERVAL))
done

echo "Finalizado: se han alcanzado los 3 minutos."
