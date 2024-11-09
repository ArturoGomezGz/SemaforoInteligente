

// Hacer una solicitud GET
function iniciarSesion() {
    let usuario = document.getElementById("username").value
    let contrasena = document.getElementById("password").value

    // URL local
    const url = 'http://127.0.0.1:5000/getUsuario/'+usuario;
    console.log(url)

  let sesion
  axios.get(url)
  .then(response => {
    // Imprimir los datos de la respuesta
    sesion = (response.data);
  })
  .catch(error => {
    // Manejo de errores
    console.error("Error fetching data:", error);
  });

  console.log(sesion[0]["id"])
}