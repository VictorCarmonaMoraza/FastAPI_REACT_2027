import os
import subprocess

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


# Cargamos las variables del archivo .env
load_dotenv()


# Obtenemos la URL de conexión desde el archivo .env
DATABASE_URL = os.getenv("DATABASE_URL")


def limpiar_alembic_version():
    """
    Comprueba si existe la tabla alembic_version.

    Si existe, muestra cuántas versiones contiene.
    """

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as connection:

            # PostgreSQL: comprobamos si existe la tabla alembic_version
            resultado = connection.execute(
                text(
                    """
                    SELECT COUNT(*)
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                    AND table_name = 'alembic_version'
                    """
                )
            )

            existe = resultado.scalar() > 0

            if existe:

                # Comprobamos si contiene alguna versión
                resultado = connection.execute(
                    text("SELECT COUNT(*) FROM alembic_version")
                )

                versiones = resultado.scalar()

                if versiones == 0:
                    print(
                        "La tabla alembic_version existe pero está vacía."
                    )
                else:
                    print(
                        "Tabla alembic_version encontrada con "
                        f"{versiones} versión(es)."
                    )

    finally:
        engine.dispose()


def ejecutar_comando(comando):
    """
    Ejecuta un comando de consola y muestra su resultado.
    """

    print(f"\nEjecutando: {' '.join(comando)}")

    resultado = subprocess.run(
        comando,
        check=True,
        text=True,
    )

    return resultado


if __name__ == "__main__":

    try:

        # Comprobamos el estado de alembic_version
        limpiar_alembic_version()

        # Generamos automáticamente una migración
        ejecutar_comando(
            [
                "alembic",
                "revision",
                "--autogenerate",
                "-m",
                "crear tabla libros",
            ]
        )

        # Aplicamos las migraciones pendientes
        ejecutar_comando(
            [
                "alembic",
                "upgrade",
                "head",
            ]
        )

        print("\nMigraciones aplicadas correctamente.")

    except subprocess.CalledProcessError as error:

        print(
            "\nError al ejecutar Alembic. "
            f"Código de salida: {error.returncode}"
        )