// Hacer una solicitud GET
function iniciarSesion() {
  let usuario = document.getElementById("username").value
  let contrasena = document.getElementById("password").value

  if (usuario == "" || contrasena == ""){
    alert("Llenar todos los campos")
    return 0
  }

  // URL local
  const url = 'http://127.0.0.1:5000/getUsuario/'+usuario;
  console.log(url)

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