import json
from fastapi import UploadFile

async def process_json_file(file: UploadFile) -> dict:
    contenido = await file.read()
    
    try:
        data = json.loads(contenido)
        tipo = type(data).__name__
        if isinstance(data, list):
            longitud = len(data)
        elif isinstance(data, dict):
            longitud = len(data.keys())
        else:
            longitud = None
        
        return {
            "tipo": "json",
            "estructura": tipo,
            "longitud": longitud,
            "preview": data if longitud and longitud < 5 else str(data)[:300]
        }
    except json.JSONDecodeError:
        return {"error": "Archivo JSON inválido"}
