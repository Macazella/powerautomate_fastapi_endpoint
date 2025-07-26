from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os

from utils.process_docx import process_docx_file
from utils.process_xlsx import process_xlsx_file
from utils.process_json import process_json_file

app = FastAPI()

@app.post("/procesar-archivo/")
async def procesar_archivo(file: UploadFile = File(...)):
    filename = file.filename.lower()
    
    if filename.endswith(".docx"):
        result = await process_docx_file(file)
    elif filename.endswith(".xlsx"):
        result = await process_xlsx_file(file)
    elif filename.endswith(".json"):
        result = await process_json_file(file)
    else:
        raise HTTPException(status_code=400, detail="Tipo de archivo no soportado.")

    return JSONResponse(content=result)
