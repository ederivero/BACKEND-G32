# from LIBRERIA import CLASES, FUNCIONES que queremos usar de la libreria
from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType
# PARA MSSQL
from mssql_python import connect as conector_mssql
connection_str = "Server=localhost,1433;Database=<database_name>;UID=<username>;PWD=<password>;Encrypt=yes;TrustServerCertificate=yes"

# conexion_mssql = conector_mssql(connection_str)

# cursor_mssql = conexion_mssql.cursor()

# PARA POSTGRES
from psycopg import connect

# postgresql://NOMBRE_USUARIO:PASSWORD_USUARIO@HOST:PUERTO/NOMBRE_BD
credenciales = "postgresql://postgres:root@127.0.0.1:5432/flask_db"
conexion = connect(conninfo=credenciales)


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
        # El encargado de iniciar la comunicacion con la BD
        cursor = conexion.cursor()

        # Ejecutamos el comando en la bd, aca no es necesario colocar ; al final
        cursor.execute("SELECT * FROM productos")

        # Para obtener el resultado (si es necesario) usamos los metodos fetchone, fetchall, fetchmany
        productos_bd = cursor.fetchall()

        print(productos_bd)
        resultado = []

        for producto in productos_bd:
            resultado.append({
                "id": producto[0],
                "nombre": producto[1],
                "precio": float(producto[2]),
                "cantidad": producto[3]
            })
            
        # Los controladores (es la logica del endpoint) suelen retornar diccionarios que estos seran interpretados en JSON o tambien se suele retornar listas (arreglos)
        return {
            "message":"Los productos son:",
            "content": resultado
        }
    
    elif request.method =='POST':
        # Se usa para crear nueva informacion proveniente del frontend
        # request.get_data() # retorna la informacion proveniente del cliente directamente como si fuese un string, sirve tambien si la informacion enviada sera un texto
        # print(request.get_data())
        # request.get_json() # retorna la informacion del cliente y la convierte a un diccionario para que python la pueda entender
        # print(request.get_json())
        try:
            data = request.get_json()
            # Ahora con la informacion correctamos agregamos este producto a nuestra lista
            productos.append(data)
            return {
                "message":"Producto creado exitosamente"
            }
        except UnsupportedMediaType:
            # Handler (manejador de errores)
            return {
                "message": "Debes enviar la informacion en formato JSON"
            }
        



# ESTO SIEMPRE VA AL FINAL!!!!!
if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    # debug significa que con cada cambio que guardemos los archivos automaticamente se reiniciara el servidor
    app.run(port=5000, debug=True)