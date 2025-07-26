from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Permitir CORS para llamadas desde Power Automate u otros orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés restringir esto si querés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz para evitar error 404 en Render
@app.get("/")
def read_root():
    return {"message": "API up and running"}

# Modelo de datos esperado
class FilePayload(BaseModel):
    filename: str
    content: str  # Puede ser texto, base64 u otra codificación

# Endpoint principal para consumir desde Power Automate
@app.post("/process_file/")
async def process_file(payload: FilePayload):
    # Podés agregar lógica de guardado, análisis o respuesta acá
    return {
        "status": "success",
        "received": {
            "filename": payload.filename,
            "content_length": len(payload.content)
        }
    }
