from django.db import models
from uuid import uuid4

class Categoria(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    habilitado = models.BooleanField(default=True) 
    eliminado  = models.BooleanField(default=False)

    class Meta:
        db_table = 'categorias'


class Media(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    ext = models.CharField(max_length=100, null=False)
    ruta = models.CharField(max_length=200, null=False)
    mimeType = models.CharField(db_column='mime_type', max_length=100, null=False)
    habilitado = models.BooleanField(default=True) 
    eliminado  = models.BooleanField(default=False)

    class Meta:
        db_table = 'medias'


class Producto(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.CharField(max_length=200, null=False)
    habilitado = models.BooleanField(default=True) 
    eliminado  = models.BooleanField(default=False)
    
    categoria = models.ForeignKey(to=Categoria, on_delete=models.PROTECT, db_column='categoria_id')
    media = models.ForeignKey(to=Media, on_delete=models.PROTECT, db_column='media_id', null=True)

    class Meta:
        db_table = 'productos'


class Precio(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    habilitado = models.BooleanField(default=True) 
    eliminado  = models.BooleanField(default=False)

    producto = models.ForeignKey(to=Producto, on_delete=models.PROTECT, db_column='producto_id')

    class Meta:
        db_table = 'precios'
