function iniciarSesion(){
    let usuario = document.getElementById("username").value
    let contrasena = document.getElementById("password").value
  
    if (usuario == "" || contrasena == ""){
        alert("Llenar todos los campos")
        return 0
    }
  
    // URL local
    const url = 'http://127.0.0.1:5000/getUsuario/'+usuario;
  
    axios.get(url)
    .then(response => {
        // Imprimir los datos de la respuesta
        let sesion = JSON.parse(response.data)[0];
        if (sesion){
            if (sesion["contrasena"]==contrasena){
              window.location.href = "./estadisticas.html";
            }
        }
    })
    .catch(error => {
        // Manejo de errores
        console.error("Error fetching data:", error);
    });
}

function verEstadisticas(){
    let usuario = document.getElementById("username").value
    let contrasena = document.getElementById("password").value

    const url = 'http://127.0.0.1:5000/mciclos';
    axios.get(url)
    .then(response => {
        let mCiclos = JSON.parse(response.data);
        print(mCiclos)
        const ctx1 = document.getElementById('grafico1').getContext('2d');
        const grafico1 = new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: ['Enero', 'Febrero', 'Marzo', 'Abril'],
                datasets: [{
                    label: 'Cantidad de Autos',
                    data: [12, 19, 3, 5],
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
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

        const ctx2 = document.getElementById('grafico2').getContext('2d');
        const grafico2 = new Chart(ctx2, {
            type: 'line',
            data: {
                labels: ['Enero', 'Febrero', 'Marzo', 'Abril'],
                datasets: [{
                    label: 'Flujo de Tráfico',
                    data: [2, 3, 20, 5],
                    fill: false,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    tension: 0.1
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

        const ctx3 = document.getElementById('grafico3').getContext('2d');
        const grafico3 = new Chart(ctx3, {
            type: 'pie',
            data: {
                labels: ['Comida', 'Transporte', 'Entretenimiento', 'Otros'],
                datasets: [{
                    label: 'Categorías de Gastos',
                    data: [300, 50, 100, 40],
                    backgroundColor: [
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(75, 192, 192, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 206, 86, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(75, 192, 192, 1)'
                    ],
                    borderWidth: 1
                }]
            }
        });
    })
    .catch(error => {
        // Manejo de errores
        console.error("Error fetching data:", error);
    });
}

function verIntersecciones(){
    const select = document.getElementById("interseccion");
    let options;

    const url = 'http://127.0.0.1:5000/intersecciones';
    axios.get(url)
    .then(response => {
        // Parse response data
        options = JSON.parse(response.data);
        console.log(options);
        options.forEach(optionData => {
            // Create an <option> element
            const option = document.createElement("option");
            option.value = optionData.id;
            option.text = 'Interseccion ' + optionData.id;
            select.appendChild(option);
        });
    })
    .catch(error => {
        // Error handling
        console.error("Error fetching data:", error);
    });
}


verIntersecciones()