fetch("http://localhost:8000/api/usuarios")
  .then(res => res.json())
  .then(usuarios => {
    if (usuarios.length > 0) {
      document.getElementById("mensaje").innerText =
        `Bienvenido, ${usuarios[0].nombre}`;
    }
  })
  .catch(err => {
    document.getElementById("mensaje").innerText = "Error al cargar usuario";
    console.error(err);
  });