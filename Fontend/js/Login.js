const formulario = document.querySelector("form");

formulario.addEventListener("submit", function(e) {
    e.preventDefault();

    const inputs = formulario.querySelectorAll("input");

    const correo = inputs[0].value;
    const password = inputs[1].value;

    const usuario = JSON.parse(localStorage.getItem("usuario"));

    if (!usuario) {
        alert("No hay usuarios registrados");
        return;
    }

    if (correo === usuario.correo && password === usuario.password) {

        localStorage.setItem("sesion", "activa");

        alert("Bienvenido " + usuario.nombre1);

        window.location.href = "Home.html";

    } else {
        alert("Correo o contraseña incorrectos");
    }
});