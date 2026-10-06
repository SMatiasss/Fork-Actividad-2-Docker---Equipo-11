from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_usuarios_responde_200():
    response = client.get("/api/usuarios")
    assert response.status_code == 200


def test_usuarios_devuelve_lista_con_datos_de_init_sql():
    data = client.get("/api/usuarios").json()
    assert isinstance(data, list)
    assert len(data) == 3


def test_usuario_tiene_campos_esperados():
    usuario = client.get("/api/usuarios").json()[0]
    assert set(usuario.keys()) == {"id", "nombre", "email"}


def test_usuarios_incluye_juan_perez():
    nombres = [u["nombre"] for u in client.get("/api/usuarios").json()]
    assert "Juan Perez" in nombres


def test_ruta_inexistente_devuelve_404():
    assert client.get("/api/no-existe").status_code == 404
