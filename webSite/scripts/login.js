let usuario = document.getElementById("username")
let contrasena = document.getElementById("password")

// URL local
const url = 'http://127.0.0.1:5000/getUsuario/'+usuario;

// Hacer una solicitud GET
function iniciarSesion() {
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

  console.log(sesion["id"])
}