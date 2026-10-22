from django.urls import path
from .views import CategoriasView

urlpatterns = [
    # as_view convierte la vista creada con DRF a una vista que la pueda entender Django y pueda servirla
    path('categorias', CategoriasView.as_view())
]