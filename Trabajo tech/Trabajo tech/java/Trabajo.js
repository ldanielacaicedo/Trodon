const toggleButton = document.getElementById('toggle-button');
const body = document.body;

toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    // Cambia la imagen según el modo
    if (body.classList.contains('dark-mode')) {
        toggleButton.src = 'imagenes/Blanco Negro.png'; // Cambia a una imagen de luna
    } else {
        toggleButton.src = 'imagenes/Blanco Negro.png'; // Cambia a una imagen de sol
    }
});
