from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class LibroSchema(BaseModel):
    # Si vamos querer convertir la informacion de instancias (del modelo) a diccionario entonces tenemos que modificar la configuracion de todo el schema indicandole que ahora tambien podremos recibir la informacion proveniente de las instancias
    model_config = ConfigDict(from_attributes=True)

    id: int | None =Field(default=None)
    nombre: str = Field(min_length=1)
    fechaPublicacion: date | None = Field(default=None)
    prologo: str | None
    isbn: str = Field(max_length=20)
    # Esta propiedad no debe ser utilizada por el cliente, jamas la debe observar
    # eliminado: bool = Field(default=False, exclude=True)