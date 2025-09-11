from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Crea la instancia de la aplicación
app = FastAPI()

# Configuración de CORS para permitir peticiones desde el frontend
origins = [
    "http://localhost",  # Para pruebas locales
    "https://mi-app-web-fastapi.onrender.com",  # La URL de tu API
    "https://guvizca.github.io/tu-repositorio-del-frontend" # **IMPORTANTE**: Aquí debes poner la URL de tu front-end en GitHub Pages
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz. Retorna un mensaje simple.
@app.get("/")
def read_root():
    return {"message": "¡Hola, mundo! Esto es mi API con FastAPI."}

# Endpoint para saludar a una persona por su nombre
@app.get("/saludo/{nombre}")
def saludar_nombre(nombre: str):
    return {"message": f"¡Hola, {nombre}! Bienvenido a la API."}
