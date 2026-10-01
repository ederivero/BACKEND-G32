from pydantic import BaseModel, ConfigDict, Field, PositiveInt, field_validator
from typing import Annotated

# Annotated agrega informacion adicional a un tipo de datos, pertenece al modulo nativo de python
# En el anotated estamos indicando que ListaIds sera de tipo list[PositiveInt] y ademas estaremos agregando el argumento para pydantic que este sera tambien un tipo Field con una longitud minima de 1 y maxima de 100
ListaIds = Annotated[list[PositiveInt], Field(min_length=1, max_length=100)]

class LibrosCategoriasSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    libroId: int = Field(min=1)
    categoriaIds: ListaIds = Field()

    # Si queremos agregar alguna validacion a alguna de las propiedades del schema podemos hacerlo mediante el decorador y en su parametro indicar que propiedad o propiedades vamos a agregar esa validacion
    @field_validator('categoriaIds')
    def eliminar_duplicados(cls, valor):
        # cls > Es la misma instancia de la clase del atributo que en este caso seria Field
        # valor > es el valor que sera validado
        # al convertilo en un diccionario temporar lo que hace es que si la llave ya existe la sobreescribe y por ende al momento de retornar las llaves no habra ninguna llave repetida y luego eso lo convertimos a una lista
        # valor > [1,1,2,3,4,4,2,5]
        # el metodo fromkeys de un diccionario crea un nuevo diccionario usando los valores de la lista como llaves y sus valores son None
        # al usar un diccionario para convertirlo a lista agarra esas llaves y las colocara en la nueva lista, y sus valores los desechara
        # IDEAR OTRA FORMA EN LA CUAL PODAMOS RETIRAR LOS VALORES DUPLICADOS DE UNA LISTA
        # resultado = []
        # for elemento in valor:
        #     if elemento not in resultado:
        #         resultado.append(elemento)
        # return resultado

        # return list(dict.fromkeys(valor))
        return list(set(valor))
    