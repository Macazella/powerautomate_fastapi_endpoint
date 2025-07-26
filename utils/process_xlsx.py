import pandas as pd
from fastapi import UploadFile
import os
import tempfile

async def process_xlsx_file(file: UploadFile) -> dict:
    contents = await file.read()
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    df = pd.read_excel(tmp_path)
    os.remove(tmp_path)

    resumen = df.describe(include='all').to_dict()

    return {
        "tipo": "xlsx",
        "columnas": list(df.columns),
        "resumen_estadistico": resumen
    }

