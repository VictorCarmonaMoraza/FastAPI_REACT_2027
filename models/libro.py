from sqlalchemy import Column, Integer, String, Float
from database import Base

class Libro(Base):
    """
    Modelo SQLAlchemy que representa la tabla 'libros'.
    """
    __tablename__ = "libros"

    # ID autoincremental y llave primaria
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Titulo del libro(Cadena obligatoria)
    titulo = Column (String(255),nullable=False)

    # Autor del libro(Cadena obligatoria)
    autor = Column(String(255),nullable=False)

    # Rating entre 1 y 5 (entero obligatorio)
    rating = Column(Float, nullable=False)