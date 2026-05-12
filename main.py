from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montamos el directorio actual para servir el index.html, styles.css y script.js
app.mount("/", StaticFiles(directory=".", html=True), name="static")
