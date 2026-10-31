from django.urls import path
from .views import (CategoriasView, 
                    DevolverActualizarEliminarCategoriaView, 
                    ProductosView,
                    ProductoView, 
                    crearUrlParaSubirArchivo,
                    crearMedia,
                    PreciosView)

urlpatterns = [
    # as_view convierte la vista creada con DRF a una vista que la pueda entender Django y pueda servirla
    path('categorias', CategoriasView.as_view()),
    # si le vamos a poner otro parametro que no se llame 'pk' entonces debo de modificar el looup_field indicando el mismo nombre
    path('categoria/<id>',DevolverActualizarEliminarCategoriaView.as_view()),
    # En las viewSet se tiene que enlazar los verbos http (GET, POST, PUT, DELETE) con los metodos declarados en la clase, porque no se hace automaticamente
    path('productos', ProductosView.as_view({
        "get":"list",
        "post":"create"
    })),
    path('producto/<id>', ProductoView.as_view({
        "get":"retrieve",
        "delete":"destroy"
    })),
    path('generar-url',crearUrlParaSubirArchivo),
    path('media',crearMedia),
    path('precios', PreciosView.as_view())
]