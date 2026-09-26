from pydantic import BaseModel, Field

# pydantic valida la configuracion que nosotros definamos en los atributos de la clase, es decir, utilizara la configuracion de cada atributo para que cuando le pasemos la informacion esta sera corroborada y si es valida, continuara, sino emitira un error de validacion
class CategoriaSerializer(BaseModel):
    nombre: str = Field(examples=["Ciencia Ficcion","Comedia"])
