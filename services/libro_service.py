# Capa de servicios encargada de la logica relacionada con libros

from sqlalchemy.orm import Session
from models.libro import  Libro
from schemas.schemas import LibroCreate


def listar_libros(db:Session):
    """
    Devuelve una lista con todos los libros almacenados en la base de datos

    Parametros:
     db(Session): Session de base de datos proporcionada por FastAPI

    Retorna:
        Lista de instancias del modelo Libro
    """
    return db.query(Libro).all()


def crear_libro(db:Session, datos:LibroCreate):
    """
    Crea un nuevo libro en la base de datos usando los datos validados
    del esquema LibroCreate
    """

    #Crear instancia del modelo usando los datos recibidos
    nuevo_libro =Libro(
        titulo = datos.titulo,
        autor= datos.autor,
        rating = datos.rating
    )
    #Guardar en la base de datos
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)

    return nuevo_libro


def buscar_por_id(db:Session, id:int) -> Libro | None:
    """
    Busca un libro por su id.

    Devuelve el libro si existe.
    Si no existe, devuelve None.
    """
    return db.query(Libro).filter(Libro.id == id).first()









