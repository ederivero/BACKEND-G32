from django.urls import path
from .views import UsuariosView

urlpatterns = [
    path('registro', UsuariosView.as_view())
]