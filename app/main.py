from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

# Cargar variables de entorno
load_dotenv()

# Modelo y API config
MODELO = os.getenv("MODELO", "deepseek-r1")

app = FastAPI()

# Configure templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class Pregunta(BaseModel):
    texto: str

@app.post("/preguntar")
async def preguntar(pregunta: Pregunta):
    try:
        # Enviar solicitud POST al servidor de Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODELO,
                "prompt": pregunta.texto,
                "stream": False
            }
        )

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al comunicarse con Ollama")

        data = response.json()
        return {"respuesta": data.get("response", "Sin respuesta del modelo")}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
