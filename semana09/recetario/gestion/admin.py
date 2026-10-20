from django.contrib import admin
from .models import Ingrediente, Preparacion, Receta

# Aca se declara todos los modelos que puede ser accedidos desde el panel administrativo
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
    # Modificar la configuracion del Ingrediente a su gusto
    list_display = ["descripcion", "cantidad"]
    # cuando se quiere buscar una fk no se puede declarar directamente sino que se tiene que usar su referencia al modelo adyacente
    # al momento de referenciar al modelo de la fk se pone el nombre de la FK y luego doble sub guion y luego el nombre de la columna que queremos usar para la busqueda
    search_fields = ["cantidad", "descripcion", "recetaId__titulo"]

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    # Que columnas puedo visualizar en la lista
    list_display = ["id", "titulo", "descripcion", "habilitado"]
    # Opciones de filtros de las columnas en la barra lateral
    list_filter = ["habilitado"]
    # Al definir se hara la busqueda en las columnas declaradas
    search_fields = ["titulo", "descripcion"]
    # Permite editar campos en la lista sin la necesidad de ingresar a su detalle
    list_editable = ["habilitado"]
    # Modifica el ordenamiento predeterminado o indicado en el modelo en el panel administrativo
    ordering = ["-titulo"]
    # Bloquea la edicion y creacion de determinados campos
    # readonly_fields = ["titulo"]


@admin.register(Preparacion)
class PreparacionAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]