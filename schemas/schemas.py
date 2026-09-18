# Importamos las herramientas de Pydantic que vamos a utilizar
from pydantic import BaseModel, Field, field_validator

# Optional permite indicar que un campo puede tener un valor o None
from typing import Optional


# ============================================================
# LIBRO BASE
# ============================================================

class LibroBase(BaseModel):
    """
    Esquema base con los campos comunes a creación y actualización.
    Incluye las validaciones de los datos.
    """

    # Campo obligatorio de tipo texto.
    # ... significa que es obligatorio.
    # min_length=1 indica que debe tener al menos un carácter.
    titulo: str = Field(
        ...,
        min_length=1,
        description="Título del libro"
    )

    # Campo obligatorio de tipo texto.
    autor: str = Field(
        ...,
        min_length=1,
        description="Autor del libro"
    )

    # Campo obligatorio de tipo entero.
    # ge=1 -> mayor o igual que 1
    # le=5 -> menor o igual que 5
    # Por tanto, el rating debe estar entre 1 y 5.
    rating: float = Field(
        ...,
        ge=1,
        le=5,
        description="Calificación del 1 al 5"
    )

    # Validador adicional para comprobar que título y autor
    # no contienen únicamente espacios.
    @field_validator("titulo", "autor")
    def no_vacios(cls, valor):

        # strip() elimina los espacios del principio y del final.
        # Si después de eliminarlos no queda nada, el campo está vacío.
        if not valor.strip():

            # Lanzamos un error de validación.
            raise ValueError("El campo no puede estar vacío")

        # Si la validación es correcta, devolvemos el valor.
        return valor


# ============================================================
# LIBRO CREATE
# ============================================================

class LibroCreate(LibroBase):
    """
    Esquema utilizado cuando queremos CREAR un libro.

    Hereda todos los campos y validaciones de LibroBase:
        - titulo
        - autor
        - rating
        - validación de campos vacíos
    """

    # No necesitamos añadir nada porque LibroCreate
    # hereda todo de LibroBase.
    pass


# ============================================================
# LIBRO UPDATE
# ============================================================

class LibroUpdate(LibroBase):
    """
    Esquema utilizado cuando queremos ACTUALIZAR un libro.

    En una actualización permitimos modificar solo algunos campos,
    por eso los campos son opcionales.
    """

    # Optional[str] significa:
    # puede ser un texto (str) o puede ser None.
    #
    # Field(None) indica que por defecto el valor será None.
    titulo: Optional[str] = Field(
        None,
        min_length=1
    )

    # El autor también es opcional.
    autor: Optional[str] = Field(
        None,
        min_length=1
    )

    # El rating también es opcional,
    # pero si se proporciona debe estar entre 1 y 5.
    rating: Optional[float] = Field(
        None,
        ge=1,
        le=5
    )

    # Validador para título y autor.
    @field_validator("titulo", "autor")
    def no_vacios_opcionales(cls, valor):

        # Primero comprobamos que el valor NO sea None.
        #
        # Si es None, lo aceptamos porque el campo es opcional.
        #
        # Si tiene un valor, comprobamos que no sean
        # únicamente espacios.
        if valor is not None and not valor.strip():

            # Si está vacío, lanzamos un error.
            raise ValueError("El campo no puede estar vacío")

        # Si todo es correcto, devolvemos el valor.
        return valor


# ============================================================
# LIBRO READ
# ============================================================

class LibroRead(BaseModel):
    """
    Esquema utilizado para devolver un libro como respuesta
    desde la API.

    Incluye el ID que genera la base de datos.
    """

    # Identificador del libro
    id: int

    # Título del libro
    titulo: str

    # Autor del libro
    autor: str

    # Calificación del libro
    rating: float

    # Permite que Pydantic pueda crear este esquema
    # a partir de un objeto ORM de SQLAlchemy.
    #
    # Por ejemplo:
    # objeto SQLAlchemy -> LibroRead
    model_config = {
        "from_attributes": True
    }