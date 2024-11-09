// Nombre de usuario que deseas buscar
const usuario = 'testing';

// Realiza una solicitud GET a la API
fetch(`127.0.0.1:5000/getUsuario/${usuario}`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Usuario no encontrado');
    }
    return response.json(); // Convierte la respuesta a JSON
  })
  .then(data => {
    console.log('Datos del usuario:', data); // Imprime los datos en la consola o úsalos en tu aplicación
  })
  .catch(error => {
    console.error('Error:', error); // Muestra el error si ocurre algún problema
  });
