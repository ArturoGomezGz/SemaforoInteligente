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

function crearUsuario() {
    let usuario = document.getElementById("usuarioCreacion").value;
    let contrasena = document.getElementById("contrasenaCreacion").value;
    let nombre = document.getElementById("nombreCreacion").value;
    let url = 'http://127.0.0.1:5000/new_user/' + usuario + '/' + contrasena + '/' + nombre;

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
        axios.post(url)
            .then(response => {
                alert("Usuario creado exitosamente");
            })
            .catch(error => {
                console.error("Error creating user:", error);
            });
    }
}

//-------------------------------


function verEstadisticas() {
    let interseccion = document.getElementById("interseccion").value
    let dia = document.getElementById("fecha").value.toString()
    let timeIni = document.getElementById("horaInicio").value.toString()
    let timeFin =document.getElementById("horaFin").value.toString()

    const url2 = 'http://127.0.0.1:5000/carSumRange/'+interseccion+'/'+timeIni+'/'+timeFin+'/'+dia;
    axios.get(url2)
        .then(response => {
            
            let suma = JSON.parse(response.data)
            
            let labels = []
            let values = []
            for (let index = 0; index < suma.length; index++) {
                labels.push("Semaforo " + index+1); 
                values.push(suma[index].noCarros)
            }
            mostrarGrafico(labels, values,1, 'bar')
            mostrarGrafico(["palabras","palabras"],[4,2],2, 'line')

        })
        .catch(error => {
            console.error("Error fetching mciclos data:", error);
        });
}

// Función para mostrar gráficos
function mostrarGrafico(labels, data, idGrafico, tipo) {
    const ctx1 = document.getElementById('grafico'+idGrafico).getContext('2d');
    const grafico1 = new Chart(ctx1, {
        type: tipo,
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de Autos',
                data: data,
                backgroundColor: 'rgba(74, 192, 192, 0.2)', // Añade el canal alfa para transparencia
                borderColor: 'rgba(74, 192, 192, 1)', // Color completo de borde
                borderWidth: 1
            }]
            
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
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
        for (let i = 0; i < mCiclos.length; i++) {
            if (i > 5){break}
            const element = mCiclos[i]; // Obtenemos el objeto de la element actual
            const fila = document.createElement("tr"); // Creamos una nueva fila
    
            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el nombre
            fila.appendChild(celdaId);

            const celdaIdInterseccion = document.createElement("td");
            celdaIdInterseccion.textContent = element.idInterseccion; // Añadimos el nombre
            fila.appendChild(celdaIdInterseccion);

            const celdaDia = document.createElement("td");
            celdaDia.textContent = element.dia; // Añadimos el nombre
            fila.appendChild(celdaDia);

            const celdaHora = document.createElement("td");
            celdaHora.textContent = element.hora; // Añadimos el nombre
            fila.appendChild(celdaHora);

            tBodyMCiclo.appendChild(fila);
        }

        const tBodyDCiclo = document.getElementById("dt-dciclo");
        for (let i = 0; i < dCiclos.length; i++) {
            if (i > 4){break}
            const element = dCiclos[i]; // Obtenemos el objeto de la element actual
            const fila = document.createElement("tr"); // Creamos una nueva fila
    
            const celdaId = document.createElement("td");
            celdaId.textContent = element.id; // Añadimos el nombre
            fila.appendChild(celdaId);

            const celdaIdCiclo = document.createElement("td");
            celdaIdCiclo.textContent = element.idCiclo; // Añadimos el nombre
            fila.appendChild(celdaIdCiclo);

            const celdaIdSemaforo = document.createElement("td");
            celdaIdSemaforo.textContent = element.idSemaforo; // Añadimos el nombre
            fila.appendChild(celdaIdSemaforo);

            const celdaNoCarros = document.createElement("td");
            celdaNoCarros.textContent = element.noCarros; // Añadimos el nombre
            fila.appendChild(celdaNoCarros);

            tBodyDCiclo.appendChild(fila);
        }
    } catch (error){
        console.error("Error loading database:", error);
    }
}


verIntersecciones()

loadDataBase()