# FROM desde que imagen vamos a partir
FROM python:3.16-rc-slim

# ENV configuramos variables de entorno en el contenedor
# Si se quiere continuar escribiendo en las lineas continuas sin importar el enter podemos colocar un \
# PYTHONDONTWRITEBYTECODE Evita que python cree archivos .pyc y carpetas __pycache__
# PYTHONUNBUFFERED Desactiva el bufer de salida de python ya que con el buffer activo python acumula los print y logs antes de enviarlos en cambio si se desactiva los mensajes salen de inmediato
ENV PYTHONDONTWRITEBYTECODE=1 \ 
    PYTHONUNBUFFERED=1

# Esto creara en el contenedor una carpeta donde se almacenara todos los archivos del proyecto y no interferira con la imagen usada como base
WORKDIR /app

# Copia el archivo/directorio indicado en la ubicacion seleccionada
COPY requirements.txt .
COPY . .

# Sirve para ejecutar un comando en la terminal del contenedor
# useradd > crea un nuevo usuario en mi contenedor app
# chown -R app:app /app > entrega las carpetas /app para que el usuario las pueda visualizar
# && ejecutar otro comando cuando el primero se ejecuto de manera exitosa
RUN useradd -m eduardo && chown -R app:app /app

# ahora asignamos el usuario que va a utilizar la aplicacion
USER eduardo

# Mi contenedor podra ser accedido desde fuera mediante un puerto expuesto, en este caso el 8000
EXPOSE 8000