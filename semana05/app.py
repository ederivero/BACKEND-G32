# from LIBRERIA import CLASES, FUNCIONES que queremos usar de la libreria
from flask import Flask

# __name__ > Variable global de python que sirve para indicar si el archivo en el cual nos encontramos se esta ejecutando directamente o no en la terminal 
# python app.py > el valor de esta variable sera __main__
# python 01.py > y dentro de este archivo mando a llamar a app.py entonces el valor de __name__ sera secondary y por ende no será el archivo principal del proyecto.
# Flask se utiliza el patrón de diseño de Singleton
app = Flask(__name__)

# Cada ruta (endpoint) Punto final (punto de acceso)
@app.route('/estado')
def estado_servidor():
    # Es de suma importancia que siempre en los endpoints retornemos algo
    return 'El servidor esta vivo!'

if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    app.run(port=5000, debug=True)