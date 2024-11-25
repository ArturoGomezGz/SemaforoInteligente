#!/bin/bash

# Rutas de los archivos de Python
script="main.py"

# Número de veces que deseas ejecutar los archivos
iterations=100  # Cambia este número según tus necesidades

python3 "api.py"

# Bucle para ejecutar los scripts n veces
for ((i=1; i<=iterations; i++))
do
    echo "Ejecución $i de $iterations"
    
    cd "semaforo"
    python3 $script
    cd ".."

done

echo "Ejecución completa."
