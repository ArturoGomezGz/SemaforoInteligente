# Semáforo Inteligente

## Descripción del Proyecto
Este proyecto implementa un **semáforo inteligente** diseñado para mejorar el flujo de tráfico en las intersecciones mediante el uso de sensores y actuadores. La principal funcionalidad es detectar la cantidad aproximada de automóviles que se encuentran en espera en cada carril de la intersección y ajustar el tiempo del semáforo de manera dinámica para optimizar el tráfico.

### Objetivo
El objetivo de este proyecto es optimizar la gestión del tráfico en las intersecciones, priorizando avenidas o calles con mayor demanda y evitando congestiones. De esta manera, se busca reducir los tiempos de espera de los conductores y mejorar el flujo vehicular.

### Características
- **Detección de Vehículos:** Utiliza un modelo entrenado para detectar y contar vehículos en tiempo real.
- **Conteo de Vehículos por Lado:** Realiza un seguimiento del número de vehículos en cada lado del semáforo.
- **Control adaptativo del semáforo:** Ajusta los tiempos de luz verde y roja en función del número de vehículos detectados.
- **Optimización del flujo vehicular:** Reduce la congestión y mejora la fluidez del tráfico en las intersecciones.
- **Interfaz Gráfica (opcional):** Posibilidad de visualizar datos en tiempo real y el estado del semáforo.

### Componentes Principales
1. **Cámara:** Para detectar el número de vehículos en cada lado.
2. **Unidad de Control:** Procesa los datos de los sensores y determina el comportamiento del semáforo.
3. **Semáforos con Actuadores:** Cambian los tiempos de espera y controlan la señalización en tiempo real.
4. **Interfaz de Usuario:** Para la monitorización y ajuste manual de las configuraciones.

### Requisitos de Hardware
- Cámaras (según el diseño implementado).
- Módulo de control (como un microcontrolador o un mini PC).
- Semáforos con control programable.
- Conexiones y actuadores para los semáforos.

### Requisitos de Software
- Lenguaje de programación (Python).
- Librerias de vision artificial (OpenCV)
- Librerías para procesamiento de señales y control de hardware.

### Instalación

#### 1. Instalación de Python
Para instalar Python, sigue estos pasos:

- **Windows:**
  1. Ve al [sitio web oficial de Python](https://www.python.org/downloads/) y descarga el instalador para Windows.
  2. Ejecuta el instalador y asegúrate de seleccionar la opción "Add Python to PATH".
  3. Completa la instalación.

- **Linux:**
  1. Abre una terminal.
  2. Ejecuta el siguiente comando para instalar Python:
     ```bash
     sudo apt-get update
     sudo apt-get install python3 python3-pip
     ```

- **macOS:**
  1. Abre una terminal.
  2. Puedes instalar Python usando Homebrew. Si no tienes Homebrew, instálalo desde [aquí](https://brew.sh/).
  3. Luego, ejecuta:
     ```bash
     brew install python
     ```

#### 2. Instalación de OpenCV
Para instalar OpenCV, utiliza el siguiente comando en la terminal:

```bash
pip install opencv-python 
```


### Cómo Contribuir
Si deseas contribuir a este proyecto, puedes:
1. Revisar los [issues](#) pendientes.
2. Proponer nuevas características mediante **pull requests**.
3. Reportar problemas o sugerencias en la sección de [discusiones](#).

### Licencia
Este proyecto está bajo la licencia MIT. Para más información, revisa el archivo [LICENSE](LICENSE).

### Contacto
Si tienes dudas o sugerencias, puedes contactarnos a través del correo: `soporte@semaforo-inteligente.com`.

¡Gracias por interesarte en el proyecto!
