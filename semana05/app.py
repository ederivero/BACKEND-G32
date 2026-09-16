# from LIBRERIA import CLASES, FUNCIONES que queremos usar de la libreria
from flask import Flask, request
# request nos dara toda la informacion proveniente del cliente, y solamente puede ser llamado dentro de un controlador > https://flask.palletsprojects.com/en/stable/api/#flask.Request

# __name__ > Variable global de python que sirve para indicar si el archivo en el cual nos encontramos se esta ejecutando directamente o no en la terminal 
# python app.py > el valor de esta variable sera __main__
# python 01.py > y dentro de este archivo mando a llamar a app.py entonces el valor de __name__ sera secondary y por ende no será el archivo principal del proyecto.
# Flask se utiliza el patrón de diseño de Singleton
app = Flask(__name__)

productos = [
    {
        "id": 1, 
        "nombre":"Vaso de vidrio"
    }, 
    {
        "id":2, 
        "nombre":"Parlante"
    },
    {
        "id":3,
        "nombre":"Botella de agua"
    }]

# Cada ruta (endpoint) Punto final (punto de acceso)
@app.route('/estado')
def estado_servidor():
    # Es de suma importancia que siempre en los endpoints retornemos algo
    return 'El servidor esta vivo!'


# si no se declara el parametro methods, su valor por defecto sera 'GET'
@app.route('/productos',methods = ['GET', 'POST'])
def gestionar_productos():
    print(request.method)
    if request.method == 'GET':

        # Los controladores (es la logica del endpoint) suelen retornar diccionarios que estos seran interpretados en JSON o tambien se suele retornar listas (arreglos)
        return {
            "message":"Los productos son:",
            "content": productos
        }
    
    elif request.method =='POST':

        return {
            "message":"Producto creado exitosamente"
        }



# ESTO SIEMPRE VA AL FINAL!!!!!
if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    # debug significa que con cada cambio que guardemos los archivos automaticamente se reiniciara el servidor
    app.run(port=5000, debug=True)