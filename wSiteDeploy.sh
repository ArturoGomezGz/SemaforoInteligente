#!/bin/bash
# Ejecutar API en segundo plano
python api.py &

# Cambiar al directorio y correr el servidor HTTP
cd webSite/
python -m http.server 8000
