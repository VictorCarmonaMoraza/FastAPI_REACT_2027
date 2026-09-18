from fastapi import FastAPI

from  api.libros import router as libros_router
from fastapi.middleware.cors import CORSMiddleware

from setting.cors import  CorsConfig

#Crear instancia principal de la aplicacion
app = FastAPI(
    title = "API Biblioteca Personal",
    description="Backend REST con FastAPI para gestionar libros",
    version="1.0.0"
)


# --------------------------------------------------------------
# Configuracion de CORS
# ---------------------------------------------------------------
# Configuramos CORS
CorsConfig.configurar(app)

#Endpoint de prueba(ruta raiz)
# Sirve para verificar que la API esta viva
@app.get("/")
def raiz():
    """
    Endpoint basico que confirma que la API esta funcionando
    """
    return {"Mensaje":"API Biblioteca funcionando correctamente"}


#[NUEVO] Incluir router de libros
app.include_router(libros_router) #Nuevo
