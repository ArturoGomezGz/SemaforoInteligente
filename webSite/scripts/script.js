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

function verEstadisticas() {
    const url2 = 'http://127.0.0.1:5000/mciclos';
    axios.get(url2)
        .then(response => {
            getSemaforos().then(semaforos => {
                mostrarGrafico(semaforos,1)
                mostrarGrafico(semaforos,2)
            }).catch(error => {
                console.error("Error:", error);
            });
        })
        .catch(error => {
            console.error("Error fetching mciclos data:", error);
        });
}

// Función para mostrar gráficos
function mostrarGrafico(semaforos, idGrafico) {
    const labels = []
    for (let index = 0; index < semaforos.length; index++) {
        labels.push("Semaforo " + semaforos[index].id); 
    }
    const ctx1 = document.getElementById('grafico'+idGrafico).getContext('2d');
    const grafico1 = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de Autos',
                data: [12, 19],
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


verIntersecciones()