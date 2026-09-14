# Capa de servicios encargada de la logica relacionada con libros

from sqlalchemy.orm import Session
from models.libro import  Libro


def listar_libros(db:Session):
    """
    Devuelve una lista con todos los libros almacenados en la base de datos

    Parametros:
     db(Session): Session de base de datos proporcionada por FastAPI

    Retorna:
        Lista de instancias del modelo Libro
    """
    return db.query(Libro).all()