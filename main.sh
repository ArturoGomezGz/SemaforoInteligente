#!/bin/bash

# Rutas de los archivos de Python
script="main.py"

# Número de veces que deseas ejecutar los archivos
iterations=50  # Cambia este número según tus necesidades

# Bucle para ejecutar los scripts n veces
for ((i=1; i<=iterations; i++))
do
    echo "Ejecución $i de $iterations"
    
    # Ejecutar el primer script
    cd "simulacion"
    echo "Ejecutando $script..."
    python "$script"
    cd ".."

    # Ejecutar el segundo script
    cd "procesamiento"
    echo "Ejecutando $script..."
    python "$script"
    cd ".."
done

echo "Ejecución completa."
