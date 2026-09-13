from fastapi import FastAPI

#Crear instancia principal de la aplicacion
app = FastAPI(
    title = "API Biblioteca Personal",
    description="Backend REST con FastAPI para gestionar libros",
    version="1.0.0"
)

#Endpoint de prueba(ruta raiz)
# Sirve para verificar que la API esta viva
@app.get("/")
def raiz():
    """
    Endpoint basico que confirma que la API esta funcionando
    """
    return {"Mensaje":"API Biblioteca funcionando correctamente"}
