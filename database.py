import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Cargamos las variables definidas en el archivo .env.
#
# De esta forma no tenemos que escribir las credenciales
# directamente dentro del código Python.
load_dotenv()


# Obtenemos directamente la URL completa de conexión
# desde la variable DATABASE_URL del archivo .env.
#
# Ejemplo:
#
# mysql+pymysql://root:admin@localhost:3306/biblioteca_db
DATABASE_URL = os.getenv("DATABASE_URL")


# Obtenemos la configuración del pool de conexiones.
#
# POOL_SIZE indica el número máximo de conexiones
# que SQLAlchemy mantendrá disponibles en el pool.
#
# Si no existe la variable, utilizaremos 20 por defecto.
POOL_SIZE = int(os.getenv("POOL_SIZE", "20"))


# Obtenemos si queremos mostrar las consultas SQL.
#
# SHOW_SQL=True  -> SQLAlchemy muestra las consultas SQL.
# SHOW_SQL=False -> SQLAlchemy no muestra las consultas.
SHOW_SQL = os.getenv("SHOW_SQL", "False").lower() == "true"


# Creamos el engine de SQLAlchemy.
#
# DATABASE_URL contiene toda la información necesaria
# para conectarnos a MySQL:
#
# mysql+pymysql://usuario:password@host:puerto/base_de_datos
#
# pool_size:
#     Número de conexiones disponibles en el pool.
#
# echo:
#     Si es True, SQLAlchemy mostrará las consultas SQL
#     que ejecuta.
engine = create_engine(
    DATABASE_URL,
    pool_size=POOL_SIZE,
    echo=SHOW_SQL
)


# Creamos una fábrica de sesiones.
#
# Cada vez que necesitemos trabajar con la base de datos
# podremos crear una nueva sesión mediante SessionLocal().
#
# autocommit=False:
#     Las operaciones no se confirman automáticamente.
#
# autoflush=False:
#     Evita que SQLAlchemy haga automáticamente un flush
#     antes de determinadas operaciones.
#
# bind=engine:
#     Las sesiones utilizarán nuestro engine para conectarse
#     con MySQL.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Creamos la clase Base que utilizaremos posteriormente
# para definir nuestros modelos SQLAlchemy.
#
# En una fase posterior tendremos, por ejemplo:
#
# class Libro(Base):
#     ...
#
# SQLAlchemy utilizará Base.metadata para conocer
# las tablas definidas por nuestros modelos.
Base = declarative_base()


def get_db():
    """
    Crea una sesión de base de datos para una petición.

    La sesión se entrega mediante yield para que FastAPI
    pueda utilizarla durante la ejecución de un endpoint.

    Finalmente se cierra la sesión, incluso si durante
    la petición se produce un error.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Esta prueba permite comprobar rápidamente que Python
# puede establecer una conexión con MySQL.
#
# Se ejecuta solamente cuando lanzamos:
#
#     python database.py
#
# No realizamos ningún SELECT. Simplemente intentamos
# abrir una conexión y, si funciona, mostramos un mensaje.
if __name__ == "__main__":
    try:
        with engine.connect():
            print("Conexión con MySQL establecida correctamente.")
    except Exception as error:
        print("Error al conectar con MySQL:")
        print(error)