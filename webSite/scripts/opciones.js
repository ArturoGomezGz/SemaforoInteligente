function agregarOpciones(){
    const select = document.getElementById("interseccion");
    let options 

    const url = 'http://127.0.0.1:5000/intersecciones'
    axios.get(url)
        .then(response => {
            // Imprimir los datos de la respuesta
            options = JSON.parse(response.data)[0];
            console.log(options)
            options.forEach(optionData => {
                // Crea un elemento <option>
                const option = document.createElement("option");
                option.value = 'Interseccion '+optionData.id;
                
                select.appendChild(option);
        })
        .catch(error => {
            // Manejo de errores
            console.error("Error fetching data:", error);
        });
    });
}