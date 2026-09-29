from pydantic import BaseModel, Field, ConfigDict

# pydantic valida la configuracion que nosotros definamos en los atributos de la clase, es decir, utilizara la configuracion de cada atributo para que cuando le pasemos la informacion esta sera corroborada y si es valida, continuara, sino emitira un error de validacion
class CategoriaSerializer(BaseModel):
    # Serializador : Es el encargado de validar la data que llega de afuera y verificar si es correcta
    nombre: str = Field(examples=["Ciencia Ficcion","Comedia"])

class CategoriaDeserializer(BaseModel):
    # Deserializador: Transformar la data proveniente de mi entorno (python) y devolvera en un formato legible (dict | json)
    # model_config es un atributo propio de la clase BaseModel que sirve para modificar todo el modelo en su totalidad, y no solamente un solo atributo
    # ConfigDict > sirve para indicar que la informacion que vamos a pasarle a este deserializador se realizara en formato de instancias y no en formato de un dict
    model_config = ConfigDict(from_attributes=True)

    # A los deserializadores no es necesario agregarles restricciones ya que solo se usara para convertir la data de instancias de clases a dict
    id: int
    nombre: str

class CategoriaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    # Para cuando se intente crear una nueva categoria, el ID no debe de enviarse 
    # al poner None indicaremos que esta propiedad puede ser opcional
    id: int | None = Field(default=None)
    nombre: str = Field(min_length=1, examples=["Ciencia Ficcion", "Comedia"])