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

// ---------
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
                backgroundColor: 'rgba(75, 192, 192, 0.2)', // Añade el canal alfa para transparencia
                borderColor: 'rgba(75, 192, 192, 1)', // Color completo de borde
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
        //const intersecciones = await JSON.parse(getIntersecciones())
        //const mCiclos = await JSON.parse(getMCiclos())
        //const dCiclos = await JSON.parse(getDCiclos())
        console.log(semaforos)
        console.log(JSON.parse(semaforos))
        //console.log(intersecciones)
        //console.log(mCiclos)
        //console.log(dCiclos)
    } catch (error){
        console.error("Error loading database:", error);
    }
}


verIntersecciones()