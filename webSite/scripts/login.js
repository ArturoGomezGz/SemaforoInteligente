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
    sesion = JSON.parse(response.data)[0];
    if (sesion){
      if (sesion["contrasena"]==contrasena){
        window.location.href = "./main.html";
      }
    }
  })
  .catch(error => {
    // Manejo de errores
    console.error("Error fetching data:", error);
  });
}