from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
import os
import time

app = FastAPI()

# Permitir que el frontend (otro origen) le pegue a esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = "db"  # nombre del servicio en docker-compose, no localhost
DB_NAME = os.getenv("MYSQL_DATABASE")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Reintenta la conexión unos segundos por si MySQL tarda en levantar
engine = None
for intento in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        break
    except Exception:
        time.sleep(3)

@app.get("/api/usuarios")
def get_usuarios():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, nombre, email FROM usuarios"))
        usuarios = [dict(row._mapping) for row in result]
    return usuarios