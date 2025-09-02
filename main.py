from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Crea la instancia de la aplicación
app = FastAPI()

# Configuración de CORS para permitir peticiones desde el frontend
origins = [
    "https://nombre-de-tu-api-en-render.onrender.com", # Puerto donde correrá el frontend local
    # Cuando despliegues el frontend, agrega aquí su URL (ej. "https://mi-frontend.vercel.app")
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