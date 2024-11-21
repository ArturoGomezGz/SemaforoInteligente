// GETs a api

function getSemaforos() {
    const url1 = 'http://127.0.0.1:5000/semaforos';
    return axios.get(url1)
        .then(response => {
            // Verifica si la respuesta es una cadena y parsea si es necesario
            return typeof response.data === "string" ? JSON.parse(response.data) : response.data;
        })
        .catch(error => {
            console.error("Error fetching semaforos data:", error);
            throw error;
        });
}

function getIntersecciones() {
    const url1 = 'http://127.0.0.1:5000/intersecciones';
    return axios.get(url1)
        .then(response => {
            // Verifica si la respuesta es una cadena y parsea si es necesario
            return typeof response.data === "string" ? JSON.parse(response.data) : response.data;
        })
        .catch(error => {
            console.error("Error fetching semaforos data:", error);
            throw error;
        });
}

function getMCiclos() {
    const url1 = 'http://127.0.0.1:5000/mciclos';
    return axios.get(url1)
        .then(response => {
            // Verifica si la respuesta es una cadena y parsea si es necesario
            return typeof response.data === "string" ? JSON.parse(response.data) : response.data;
        })
        .catch(error => {
            console.error("Error fetching semaforos data:", error);
            throw error;
        });
}

function getDCiclos() {
    const url1 = 'http://127.0.0.1:5000/dciclos';
    return axios.get(url1)
        .then(response => {
            // Verifica si la respuesta es una cadena y parsea si es necesario
            return typeof response.data === "string" ? JSON.parse(response.data) : response.data;
        })
        .catch(error => {
            console.error("Error fetching semaforos data:", error);
            throw error;
        });
}

// Sesiones 
function iniciarSesion(){
    let usuario = document.getElementById("username").value
    let contrasena = document.getElementById("password").value
  
    if (usuario == "" || contrasena == ""){
        alert("Llenar todos los campos")
        return 0
    }
  
    // URL local
    let url = 'http://127.0.0.1:5000/getUsuario/'+usuario;
  
    axios.get(url).then(response => {
        // Imprimir los datos de la respuesta
        let sesion = JSON.parse(response.data)[0];
        if (sesion){
            if (sesion["contrasena"]==contrasena){
                window.location.href = "./estadisticas.html";
            }
        }
    }).catch(error => {
        // Manejo de errores
        console.error("Error fetching data:", error);
    })
}

// Ajustes

function crearUsuario() {
    let usuario = document.getElementById("usuarioCreacion").value;
    let contrasena = document.getElementById("contrasenaCreacion").value;
    let nombre = document.getElementById("nombreCreacion").value;
    let url = 'http://127.0.0.1:5000/new_user';

    // Check if any field is empty
    if (usuario === "" || contrasena === "" || nombre === "") {
        alert("Llenar todos los campos");
    } 
    // Check password length
    else if (contrasena.length < 6) {
        alert("La contraseña debe tener al menos 6 caracteres");
    } 
    // Proceed with the API call if all checks are met
    else {
        axios.post(url, {
            usuario: usuario,
            contrasena: contrasena,
            nombre: nombre
        })
        .then(response => {
            alert("Usuario creado exitosamente");
            window.location.href = "./index.html";
        })
        .catch(error => {
            console.error("Error creating user:", error);
            window.location.href = "./ajustes.html";
        });
    }
}

function setTiepoCiclo() {
    let interseccion = document.getElementById("interseccion").value;
    let tiepo = document.getElementById("tiempoCiclo").value;
    let url = 'http://127.0.0.1:5000/updateTCiclo';

    // Check if any field is empty
    if (interseccion === "" || tiepo === "") {
        alert("Llenar todos los campos");
    } else {
        // Send data as JSON in the request body
        axios.put(url, {
            interseccion: interseccion,
            tiempoCiclo: tiepo
        })
        .then(response => {
            alert("Tiempo de ciclo actualizado correctamente");
            window.location.href = "./ajustes.html";
        })
        .catch(error => {
            console.error("Error updating cycle time:", error);
            window.location.href = "./ajustes.html";
        });
    }
}


//-------------------------------
function limpiarGraficos() {
    // Obtén los elementos canvas
    const grafico1 = document.getElementById('grafico1');
    const grafico2 = document.getElementById('grafico2');
    
    // Limpia el contenido del canvas 1
    if (grafico1) {
        const contexto1 = grafico1.getContext('2d');
        contexto1.clearRect(0, 0, grafico1.width, grafico1.height);
    }

    // Limpia el contenido del canvas 2
    if (grafico2) {
        const contexto2 = grafico2.getContext('2d');
        contexto2.clearRect(0, 0, grafico2.width, grafico2.height);
    }
}

// Variables globales para almacenar los gráficos

let grafico1, grafico2, grafico3;

function mostrarGrafico(titulo, labels, data, canvas, tipo, color, borde, graficoReferencia) {
    // Si ya existe un gráfico en el canvas, destrúyelo
    if (graficoReferencia) {
        graficoReferencia.destroy();
    }

    // Crear un nuevo gráfico y actualizar la referencia
    return new Chart(canvas, {
        type: tipo,
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de Autos',
                data: data,
                backgroundColor: color,
                borderColor: borde,
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: titulo,
                    font: {
                        size: 18
                    },
                    padding: {
                        top: 10,
                        bottom: 10
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function verEstadisticas(hoy) {
    let interseccion;
    let fecha;
    let timeIni;
    let timeFin;

    if (hoy) {
        interseccion = document.getElementById("interseccion").value;
        fecha = new Date();
        const dia = fecha.getDate();
        const mes = fecha.getMonth() + 1; // Se suma 1 porque los meses comienzan desde 0
        const ano = fecha.getFullYear();
        fecha = ano + "-" + mes + "-" + dia;
        timeIni = '00:00';
        timeFin = '23:59';
    } else {
        interseccion = document.getElementById("interseccion").value;
        fecha = document.getElementById("fecha").value.toString();
        timeIni = document.getElementById("horaInicio").value.toString();
        timeFin = document.getElementById("horaFin").value.toString();
    }

    console.log(fecha);

    const url = 'http://127.0.0.1:5000/carSumRange/' + interseccion + '/' + timeIni + '/' + timeFin + '/' + fecha;
    axios.get(url)
        .then(response => {
            let suma = JSON.parse(response.data);

            let labels = [];
            let values = [];
            for (let index = 0; index < suma.length; index++) {
                labels.push("Semaforo " + (index + 1));
                values.push(suma[index].noCarros);
            }
            const ctx = document.getElementById('grafico1').getContext('2d');
            grafico1 = mostrarGrafico("Semaforos ", labels, values, ctx, 'bar', 'rgba(54, 162, 235, 0.2)', 'rgba(54, 162, 235, 1)', grafico1);
        })
        .catch(error => {
            console.error("Error fetching mciclos data:", error);
        });

    const url2 = 'http://127.0.0.1:5000/carSumRangeByCiclos/' + 1 + '/' + timeIni + '/' + timeFin + '/' + fecha;
    axios.get(url2)
        .then(response => {
            let suma = JSON.parse(response.data);

            let labels = [];
            let values = [];
            for (let index = 0; index < suma.length; index++) {
                labels.push(suma[index].hora);
                values.push(suma[index].noCarros);
            }
            const ctx = document.getElementById('grafico2').getContext('2d');
            grafico2 = mostrarGrafico("Semaforo 1", labels, values, ctx, 'line', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 99, 132, 1)', grafico2);
        })
        .catch(error => {
            console.error("Error fetching mciclos data:", error);
        });

    const url3 = 'http://127.0.0.1:5000/carSumRangeByCiclos/' + 2 + '/' + timeIni + '/' + timeFin + '/' + fecha;
    axios.get(url3)
        .then(response => {
            let suma = JSON.parse(response.data);

            let labels = [];
            let values = [];
            for (let index = 0; index < suma.length; index++) {
                labels.push(suma[index].hora);
                values.push(suma[index].noCarros);
            }
            const ctx = document.getElementById('grafico3').getContext('2d');
            grafico3 = mostrarGrafico("Semaforo 2", labels, values, ctx, 'line', 'rgba(74, 192, 192, 0.2)', 'rgba(74, 192, 192, 1)', grafico3);
        })
        .catch(error => {
            console.error("Error fetching mciclos data:", error);
        });
}


function verIntersecciones(){
    let select = document.getElementById("interseccion");
    let options;

    let url = 'http://127.0.0.1:5000/intersecciones';
    axios.get(url).then(response => {
        // Parse response data
        options = JSON.parse(response.data);
        options.forEach(optionData => {
            // Create an <option> element
            let option = document.createElement("option");
            option.value = optionData.id;
            option.text = 'Interseccion ' + optionData.id;
            select.appendChild(option);
        });
    }).catch(error => {
        // Error handling
        console.error("Error fetching data:", error);
    })
}

// Base de datos
async function loadDataBase(){
    try{
        const semaforos = await getSemaforos()
        const intersecciones = await getIntersecciones()
        const mCiclos = await getMCiclos()
        const dCiclos = await getDCiclos()

        const tBodyInterseccion = document.getElementById("dt-interseccion");
        for (let i = 0; i < intersecciones.length ; i++) {
            if (i > 4){break}
            const element = intersecciones[i]; // Obtenemos el objeto de la element actual
            const fila = document.createElement("tr"); // Creamos una nueva fila
    
            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el nombre
            fila.appendChild(celdaId);

            const celdaNoSemaforo = document.createElement("td");
            celdaNoSemaforo.textContent = element.noSemaforos; // Añadimos el nombre
            fila.appendChild(celdaNoSemaforo);

            const celdaTCiclo = document.createElement("td");
            celdaTCiclo.textContent = element.tCiclo; // Añadimos el nombre
            fila.appendChild(celdaTCiclo);

            tBodyInterseccion.appendChild(fila);
        }

        const tBodySemaforo = document.getElementById("dt-semaforo");
        for (let i = 0; i < semaforos.length; i++) {
            if (i > 4){break}
            const element = semaforos[i]; // Obtenemos el objeto de la element actual
            const fila = document.createElement("tr"); // Creamos una nueva fila
    
            // Creamos las celdas de la fila
            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el nombre
            fila.appendChild(celdaId);
    
            const celdaTVerde = document.createElement("td");
            celdaTVerde.textContent = element.tVerde; // Añadimos la edad
            fila.appendChild(celdaTVerde);
    
            const celdaTRojo = document.createElement("td");
            celdaTRojo.textContent = element.tRojo; // Añadimos la edad
            fila.appendChild(celdaTRojo);

            const celdaSaalidaY = document.createElement("td");
            celdaSaalidaY.textContent = element.salidaY; // Añadimos la edad
            fila.appendChild(celdaSaalidaY);

            const celdaScaleFactor = document.createElement("td");
            celdaScaleFactor.textContent = element.scaleFactor; // Añadimos la edad
            fila.appendChild(celdaScaleFactor);

            const celdaMinNeighbors = document.createElement("td");
            celdaMinNeighbors.textContent = element.minNeighbors; // Añadimos la edad
            fila.appendChild(celdaMinNeighbors);

            const celdaMinSize = document.createElement("td");
            celdaMinSize.textContent = element.minSize; // Añadimos la edad
            fila.appendChild(celdaMinSize);

            const celdaMaxSize = document.createElement("td");
            celdaMaxSize.textContent = element.maxSize; // Añadimos la edad
            fila.appendChild(celdaMaxSize);
    
            // Añadimos la fila completa al tBodySemaforo
            tBodySemaforo.appendChild(fila);
        }

        const tBodyMCiclo = document.getElementById("dt-mciclo");
        for (let i = 0; i < 4 && i < mCiclos.length; i++) {
            const element = mCiclos[i]; // Obtenemos el objeto del elemento actual
            const fila = document.createElement("tr"); // Creamos una nueva fila
        
            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el ID
            fila.appendChild(celdaId);
        
            const celdaIdInterseccion = document.createElement("td");
            celdaIdInterseccion.textContent = element.idInterseccion; // Añadimos el ID de la intersección
            fila.appendChild(celdaIdInterseccion);
        
            const celdaDia = document.createElement("td");
            celdaDia.textContent = element.dia; // Añadimos el día
            fila.appendChild(celdaDia);
        
            const celdaHora = document.createElement("td");
            celdaHora.textContent = element.hora; // Añadimos la hora
            fila.appendChild(celdaHora);
        
            tBodyMCiclo.appendChild(fila);
        }
        for (let i = mCiclos.length - 1; i >= mCiclos.length - 6 && i >= 0; i--) {
            const element = mCiclos[i]; // Obtenemos el objeto del elemento actual
            const fila = document.createElement("tr"); // Creamos una nueva fila

            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el ID
            fila.appendChild(celdaId);

            const celdaIdInterseccion = document.createElement("td");
            celdaIdInterseccion.textContent = element.idInterseccion; // Añadimos el ID de la intersección
            fila.appendChild(celdaIdInterseccion);

            const celdaDia = document.createElement("td");
            celdaDia.textContent = element.dia; // Añadimos el día
            fila.appendChild(celdaDia);

            const celdaHora = document.createElement("td");
            celdaHora.textContent = element.hora; // Añadimos la hora
            fila.appendChild(celdaHora);

            tBodyMCiclo.appendChild(fila);
        }


        const tBodyDCiclo = document.getElementById("dt-dciclo");
        for (let i = 0; i < 4 && i < dCiclos.length; i++) {
            const element = dCiclos[i]; // Obtenemos el objeto del elemento actual
            const fila = document.createElement("tr"); // Creamos una nueva fila

            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el ID
            fila.appendChild(celdaId);

            const celdaIdCiclo = document.createElement("td");
            celdaIdCiclo.textContent = element.idCiclo; // Añadimos el ID del ciclo
            fila.appendChild(celdaIdCiclo);

            const celdaIdSemaforo = document.createElement("td");
            celdaIdSemaforo.textContent = element.idSemaforo; // Añadimos el ID del semáforo
            fila.appendChild(celdaIdSemaforo);

            const celdaNoCarros = document.createElement("td");
            celdaNoCarros.textContent = element.noCarros; // Añadimos el número de carros
            fila.appendChild(celdaNoCarros);

            tBodyDCiclo.appendChild(fila);
        }
        for (let i = dCiclos.length - 1; i >= dCiclos.length - 6 && i >= 0; i--) {
            const element = dCiclos[i]; // Obtenemos el objeto del elemento actual
            const fila = document.createElement("tr"); // Creamos una nueva fila

            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el ID
            fila.appendChild(celdaId);

            const celdaIdCiclo = document.createElement("td");
            celdaIdCiclo.textContent = element.idCiclo; // Añadimos el ID del ciclo
            fila.appendChild(celdaIdCiclo);

            const celdaIdSemaforo = document.createElement("td");
            celdaIdSemaforo.textContent = element.idSemaforo; // Añadimos el ID del semáforo
            fila.appendChild(celdaIdSemaforo);

            const celdaNoCarros = document.createElement("td");
            celdaNoCarros.textContent = element.noCarros; // Añadimos el número de carros
            fila.appendChild(celdaNoCarros);

            tBodyDCiclo.appendChild(fila);
        }
    } catch (error){
        console.error("Error loading database:", error);
    }
}


verIntersecciones()

loadDataBase()