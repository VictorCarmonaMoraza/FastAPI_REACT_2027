from fastapi.middleware.cors import CORSMiddleware


class CorsConfig:
    """
    Configuración de CORS de la aplicación.
    """

    origins = [
        "http://localhost:4200",   # Angular
        "http://localhost:5173",   # React + Vite
    ]

    @classmethod
    def configurar(cls, app):
        """
        Configura el middleware CORS en la aplicación FastAPI.
        """

        app.add_middleware(
            CORSMiddleware,

            # Orígenes permitidos
            allow_origins=cls.origins,

            # Permitimos todos los métodos HTTP
            allow_methods=["*"],

            # Permitimos todas las cabeceras
            allow_headers=["*"],

            # Permitimos credenciales
            allow_credentials=True,
        )