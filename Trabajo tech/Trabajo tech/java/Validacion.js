document.addEventListener('DOMContentLoaded', inicio); // Evento que se dispara cuando todo el HTML ha sido cargado

function inicio() {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();

        // Obtener los valores de los campos
        const nombre = document.getElementById('nombre').value.trim(); 
        const password = document.getElementById('password').value.trim(); 

        // Limpiar mensajes de error
        document.getElementById('nombreError').style.display = 'none';
        document.getElementById('passwordError').style.display = 'none';
        let isvalid = true;

        // Validar que el  nombre no este vacio y solo contenga letras 
        const nombreRegex = /^[A-Za-z\s]+$/;
        if (nombre === "" || !nombreRegex.test(nombre)) {
            document.getElementById('nombreError').style.display = 'block';
            document.getElementById('nombreError').
            textContent = 'el nombre debe contener solo letras y no puede estar vacio. ';
            isValid = false;
        }

        // Validar que la contraseña tenga al menos 8 caracteres 
        if (password === "" || password.lenght < 8) {
            document.getElementById('passwordError').style.display = 'block';
            document.getElementById('passwordError').textContent = 'la contraseña debe tener al menos 8 caracteres.';
            isValid = false;

        }

        if (isvalid){
            alert('Incio de sesion exitoso');
            // aqui puedes agregar el codigo para enviar el formulario o continuar con la autenticacion
        }
        


    }); 
} // Cierre de la función inicio