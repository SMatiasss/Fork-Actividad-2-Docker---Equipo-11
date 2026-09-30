# Actividad 2 — Docker
**Equipo #11**

Integrantes: Victoria Camila Vallarino - David Alejandro Morales Silva - Agustina Quimey Nieva - Lautaro Marcherett

Enlace al video: https://drive.google.com/drive/folders/19GY7v0ormEq1dS01JVrRpdAmqlArOuhO?usp=sharing

Configuración completa de Docker para un proyecto Web Full-Stack: base de datos MySQL, backend en FastAPI y frontend estático servido con Nginx, conectados por una red bridge personalizada.

## Estructura de carpetas

```
actividad2/
├── backend/
│   ├── Dockerfile          # Imagen del backend (Python 3.11-slim + FastAPI)
│   ├── main.py              # Endpoint /api/usuarios, conexión a MySQL
│   └── requirements.txt     # Dependencias del backend
│
├── frontend/
│   ├── Dockerfile          # Imagen del frontend (Nginx sirviendo estáticos)
│   ├── index.html           # Página que muestra el mensaje de bienvenida
│   └── script.js            # Hace fetch() al backend y actualiza el HTML
│
├── db-init/
│   └── init.sql             # Crea la tabla "usuarios" y carga datos de ejemplo
│                             #   (se ejecuta automáticamente solo la primera vez)
│
├── docker-compose.yml       # Orquesta los 3 servicios, la red y el volumen
├── .env                     # Variables de entorno reales (NO se sube al repo)
├── .env.example              # Plantilla de las variables necesarias
└── README.md                 # Este archivo
```

## Requisitos previos

- Tener [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y corriendo (con el motor/"Engine" activo).

## Cómo levantar el entorno

1. Cloná o descargá el proyecto.
2. Copiá `.env.example` a un archivo nuevo llamado `.env` y completá los valores:
   ```bash
   cp .env.example .env
   ```
3. Parado en la carpeta raíz del proyecto (donde está el `docker-compose.yml`), ejecutá:
   ```bash
   docker compose up --build
   ```
4. Esperá a que los 3 contenedores estén arriba (vas a ver en la terminal cómo primero levanta la base de datos, luego el backend, y por último el frontend).
5. Abrí el navegador en:
   - **Frontend:** http://localhost:3000
   - **API (backend):** http://localhost:8000/api/usuarios

## Cómo apagar el entorno

```bash
docker compose down
```

Si además querés borrar los datos guardados en el volumen de MySQL (por ejemplo, para que `init.sql` se vuelva a ejecutar desde cero):

```bash
docker compose down -v
```

## Servicios

| Servicio  | Imagen / Build     | Puerto expuesto | Descripción                                  |
|-----------|--------------------|-----------------|-----------------------------------------------|
| `db`      | `mysql:8.0`        | 3306            | Base de datos MySQL con volumen persistente   |
| `backend` | `./backend`        | 8000            | API FastAPI que consulta la tabla `usuarios`  |
| `frontend`| `./frontend`       | 3000            | Página estática (Nginx) que consume la API    |

## Variables de entorno necesarias

Ver `.env.example` para el detalle completo. En resumen:

- `MYSQL_ROOT_PASSWORD`
- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
