from django.urls import path
from .views import listar_recetas

# si la variable no se llama urlpatterns django no podra encontrar el conjunto de rutas declaradas y por ende no podra ser accedidas
urlpatterns = [
    path("recetas/", listar_recetas),
]