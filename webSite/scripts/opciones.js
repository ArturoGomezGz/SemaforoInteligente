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
