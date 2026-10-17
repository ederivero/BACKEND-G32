from django.db import models
from uuid import uuid4

class Receta(models.Model):
    # https://docs.djangoproject.com/en/6.1/topics/db/models/
    # https://docs.djangoproject.com/en/6.1/ref/models/options/
    id = models.AutoField(primary_key=True, null=False)
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    habilitado = models.BooleanField(default=True)

    class Meta:
        # SIEMPRE SE LLAMA META porque En los modelos se usa para poder modificar las propiedades del modelo como su nombre de la tabla, ordenamiento
        # Metatributes 
        # https://docs.djangoproject.com/en/6.1/ref/models/options/
        db_table = 'recetas'
        # si se quiere el ordenamiento de manera asc entonces se le pone el atributo
        # y si se quiere de manera descendente se pone al comienzo un -
        ordering = ['titulo']
        # constraints sirve para poder indicar una unicidad en conjunto, es decir 
        # constraints = [['titulo','descripcion'], ['titulo','habilitado']]


class Ingrediente(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    descripcion = models.TextField(null=False)
    cantidad = models.TextField(null=False)
    # Llaves foraneas
    # on_delete y el on_update y esto se usa para las relaciones y sirven para indicar cual sera el comportamiento de la fk cuando el padre sea eliminado 
    # CASCADE > Si el padre es eliminado, automaticamente los hijos son eliminados. Si la receta se elimina, se eliminan todos los ingredientes de manera automatica
    # PROTECT > Evita la eliminacion del padre si tiene hijos. Si se quiere eliminar una Receta que tiene ingredientes no se podra
    # RESTRICT > Es igual que el protect solo que emite una excepcion de RESTRICT_VALUE_ERROR 
    # SET_DEFAULT > Se puede colocar un valor por defecto si se elimina el padre. Si elimina la receta cambiar la fk a un valor por defecto (puede ser otro padre)
    # DO_NOTHING > ES EL PEOR DE TODOS! No hace nada y permite la eliminacion del padre y el hijo seguira conservando su id. Si se elimina la receta, el ingrediente seguira conservando su id que ya no existe y generara desintegridad de datos
    # SET_NULL > Permite la eliminacion del padre y cambia el valor de la FK a null. Si se elimina el padre los ingredientes la receta_id cambiara a NULL
    recetaId = models.ForeignKey(to=Receta, on_delete=models.PROTECT, db_column='receta_id')

    class Meta:
        db_table = 'ingredientes'

class Preparacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    descripcion = models.TextField()
    orden = models.IntegerField(null=False)
    recetaId= models.ForeignKey(to=Receta, on_delete=models.PROTECT, db_column='receta_id')

    class Meta:
        db_table ='preparaciones'
        # Unicidad en conjunto indicando que el orden y la recetaId no se puede repetir
        # orden | recetaId
        #   1   |    1
        #   2   |    1
        #   1   |    2
        #   2   |    1 [X]
        # https://docs.djangoproject.com/en/6.1/ref/models/options/#unique-together
        unique_together = [['orden','recetaId']]