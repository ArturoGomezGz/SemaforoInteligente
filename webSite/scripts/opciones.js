const select = document.getElementById("interseccion");
let options;

const url = 'http://127.0.0.1:5000/intersecciones';
axios.get(url)
    .then(response => {
        // Parse response data
        options = response.data;
        console.log(options);
        options.forEach(optionData => {
            // Create an <option> element
            const option = document.createElement("option");
            option.value = 'Interseccion ' + optionData.id;
            option.text = optionData.name;  // Adjust this to match the property you want as text
            select.appendChild(option);
        });
    })
    .catch(error => {
        // Error handling
        console.error("Error fetching data:", error);
    });
