from django.urls import path
from .views import registroUsuario, perfilUsuario, loginManual
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro', registroUsuario),
    path('perfil',perfilUsuario),
    path('login-libreria', TokenObtainPairView.as_view()),
    path('login', loginManual),
]