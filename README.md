
```markdown
# Endpoint FastAPI para Power Automate

Este repositorio contiene una API REST desarrollada con **FastAPI**, diseñada para integrarse con flujos automatizados de **Power Automate**, permitiendo el procesamiento de archivos enviados desde SharePoint o correo electrónico.

## 🚀 Funcionalidad

- ✅ Recibe archivos `.docx` vía solicitud `POST` desde Power Automate.
- ✅ Extrae texto y estructura mediante la librería `python-docx`.
- ✅ Procesa y transforma el contenido con funciones auxiliares en `utils/`.
- ✅ Devuelve un JSON estructurado como respuesta para ser consumido en los flujos.
- ✅ Puede desplegarse automáticamente en **Render** mediante `render.yaml`.

## 📁 Estructura del proyecto

```

📦 PRUEBA/
├── main.py              # Archivo principal con FastAPI
├── utils/               # Módulo con funciones de procesamiento
├── requirements.txt     # Dependencias del proyecto
├── render.yaml          # Configuración para Render
└── .gitignore

````

## ▶️ Ejecución local

1. Crear entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
````

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:

   ```bash
   uvicorn main:app --reload
   ```

4. Acceder a la documentación interactiva:

   * 📎 [http://localhost:8000/docs](http://localhost:8000/docs)

## 🌐 Despliegue en Render

* Crear un nuevo servicio en [https://render.com](https://render.com)
* Conectar el repositorio
* Render detectará `render.yaml` y configurará automáticamente:

  * Entorno: Python 3.10
  * Comando: `uvicorn main:app --host 0.0.0.0 --port 10000`

## 🔗 Aplicación en flujos Power Automate

Este endpoint puede ser consumido desde flujos de Power Automate (cloud o desktop), enviando archivos desde:

* SharePoint
* Outlook
* OneDrive
* Cualquier otra fuente compatible

### Ejemplo:

📤 Trigger en SharePoint: al cargar un archivo
🔁 Acción HTTP: llamada POST al endpoint
📥 Respuesta: JSON con contenido procesado, reutilizable en siguientes pasos del flujo

---

## 🧠 Sobre el proyecto

Este desarrollo es parte de un proyecto personal de automatización aplicable a entornos corporativos, orientado a **Desarrolladores Power Platform**, **Ingenieros de Datos** y **Analistas BI**.

## 📬 Contacto

**Magalí Cazella**
🔹 BI Developer | Automatización | Power Automate | FastAPI
🔗 LinkedIn: https://www.linkedin.com/in/magali-cazella-mendez/

```

---

