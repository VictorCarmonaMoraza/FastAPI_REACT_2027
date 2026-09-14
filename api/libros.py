

#Router encargado de exponer la rutas relacionadas con libros

from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.libro_service import listar_libros
from schemas.schemas import LibroRead


#Crear router con prefijo y etiquetas
router = APIRouter(
    prefix="/api/libros",
    tags=["Libros"]
)


# Decorador
@router.get("/", response_model=List[LibroRead])
def obtener_libros(db:Session=Depends(get_db)):
    """
    Endpoint que devuelve la lista completa de libros.
    Utiliza la capa de servicios para acceder a la base de datos
    """
    libros= listar_libros(db)
    return libros


