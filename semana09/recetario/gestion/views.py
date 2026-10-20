from django.shortcuts import render
from .models import Receta

def listar_recetas(request):
    # SELECT * FROM recetas;
    recetas = Receta.objects.all()
    return render(request, "lista_recetas.html", {"recetas": recetas})