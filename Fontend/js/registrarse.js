const formulario = document.querySelector("form");

formulario.addEventListener("submit", function(e) {
    e.preventDefault();

    const inputs = formulario.querySelectorAll("input");

    const nombre1 = inputs[0].value;
    const nombre2 = inputs[1].value;
    const apellido1 = inputs[2].value;
    const apellido2 = inputs[3].value;
    const correo = inputs[4].value;
    const password = inputs[5].value;
    const confirmar = inputs[6].value;

    if (password !== confirmar) {
        alert("Las contraseñas no coinciden");
        return;
    }

    const usuario = {
        nombre1,
        nombre2,
        apellido1,
        apellido2,
        correo,
        password
    };

    localStorage.setItem("usuario", JSON.stringify(usuario));

    alert("Registro exitoso");

    window.location.href = "InicioS.html";
});