

#Router encargado de exponer la rutas relacionadas con libros

from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from services.libro_service import listar_libros,crear_libro
from schemas.schemas import LibroRead, LibroCreate

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


@router.post("/",response_model=LibroRead,status_code=201)
def crear_libro_enpoint(datos:LibroCreate,db:Session=Depends(get_db)):
    """
    Crea un nuevo libro en la base de datos
    Recibe un cuerpo JSON validado con LibroCreate
    """
    nuevo_libro = crear_libro(db,datos)
    return nuevo_libro


