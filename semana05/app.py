# from LIBRERIA import CLASES, FUNCIONES que queremos usar de la libreria
from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType
from dotenv import load_dotenv
from flask_cors import CORS
from os import environ # devolvera todas las variables de entorno de la maquina y aqui se agregaran las variables del archivo .env

# el load_dotenv SIEMPRE debe ir en la primera linea del proyecto para que cargue todas las variables en todo el proyecto y evitar alguna variable no leida
load_dotenv()

# PARA MSSQL
from mssql_python import connect as conector_mssql
connection_str = environ.get("DATABASE_URL")

# conexion_mssql = conector_mssql(connection_str)

# cursor_mssql = conexion_mssql.cursor()

# PARA POSTGRES
from psycopg.rows import dict_row
from psycopg import connect

# postgresql://NOMBRE_USUARIO:PASSWORD_USUARIO@HOST:PUERTO/NOMBRE_BD
credenciales = environ.get("DATABASE_URL")
conexion = connect(conninfo=credenciales)


# request nos dara toda la informacion proveniente del cliente, y solamente puede ser llamado dentro de un controlador > https://flask.palletsprojects.com/en/stable/api/#flask.Request

# __name__ > Variable global de python que sirve para indicar si el archivo en el cual nos encontramos se esta ejecutando directamente o no en la terminal 
# python app.py > el valor de esta variable sera __main__
# python 01.py > y dentro de este archivo mando a llamar a app.py entonces el valor de __name__ sera secondary y por ende no será el archivo principal del proyecto.
# Flask se utiliza el patrón de diseño de Singleton
app = Flask(__name__)

# https://flask-cors.corydolphin.com/extension/
CORS(app, origins=['http://127.0.0.1:5500'], methods=['GET','POST','PUT','DELETE'])



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

        # Finaliza la comunicacion con la base de datos
        cursor.close()

        resultado = []

        for producto in productos_bd:
            # Primer metodo con if-else
            # precio = 0
            # if producto[2]:
            #     precio = float(producto[2])
            # else:
            #     precio = None

            # resultado.append({
            #     "id": producto[0],
            #     "nombre": producto[1],
            #     # Validar si el producto[2] no esta vacio convertirlo a float, caso contrario, devolver el valor actual
            #     "precio": precio,
            #     "cantidad": producto[3]
            # })

            # Segundo metodo con operador ternario
            resultado.append({
                "id": producto[0],
                "nombre": producto[1],
                # Validar si el producto[2] no esta vacio convertirlo a float, caso contrario, devolver el valor actual
                "precio": float(producto[2]) if producto[2] else producto[2],
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

            cursor = conexion.cursor()

            # El %s hace la conversion de la informacion proveniente del cliente a un string sin parametros que puedan vulnerar mi base de datos y en los string comunes podemos usar %f para flotantes y adicionalmente el %i para convertir a enteros y asi podemos evitar ataques directos a la base de datos (SQL INYECTION)
            # Si queremos retornar la informacion que acabamos de grabar en la base de datos se puede utilizar el comando RETURNING columnas, es decir, si ponemos INSERT INTO ... VALUES ... RETURNING * esto devolvera toda la informacion agregada a la bd
            # https://www.psycopg.org/psycopg3/docs/basic/params.html
            cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s) RETURNING *",(
                data.get("nombre"), 
                data.get("precio"), 
                data.get("cantidad")))

            # Para conservar la data y asegurarnos de que se guarde la informacion de manera permanente en la bd
            conexion.commit()

            # Para obtener el nuevo producto creado
            nuevo_producto = cursor.fetchone()

            print(nuevo_producto)

            cursor.close()
            return {
                "message":"Producto creado exitosamente"
            },201 # Created (Creado)
        except UnsupportedMediaType:
            # Handler (manejador de errores)
            return {
                "message": "Debes enviar la informacion en formato JSON"
            }, 400 # Bad request (Mala solicitur)
        

# En el endpoint cuando se coloca <variable> significa que esa parte recibira un valor diferente y ese valor se almacenara en la variable con ese nombre 
@app.route('/producto/<id>', methods = ['GET', 'PUT', 'DELETE'])
def gestionar_producto_por_id(id):
    if request.method == 'GET':
        cursor = conexion.cursor(row_factory=dict_row)
        cursor.execute("SELECT * FROM productos WHERE id = %s",(id,))

        resultado = cursor.fetchone()

        print(resultado)

        cursor.close()

        # Si el producto no existe retornar un mensaje que el producto no existe, caso contrario mostrar el mensaje ok
        if not resultado:
            return {
                "message":"Producto no encontrado"
            }, 404 # Not found (no encontrado)

        # En mssql-python (SQL SERVER) ya viene implementada la funcion de diccionario, es decir al ingresar al resultado puedo acceder como si fueran atributos como por ejemplo resultado.get("id")

        return {
            "content": resultado
        }

    elif request.method == 'PUT':
        # cuando tenemos un error en unuestra operacion y hacemos un commit se queda "pegado" y no permite realizar otra operacion ya que esta bloqueado, entonces para liberar esa operacion y dejarla sin efecto usamos el rollback para deshacer todos los cambios y si no hay ningun error no tendra efecto este comando pero tampoco lanzara error
        conexion.rollback()

        cursor = conexion.cursor(row_factory=dict_row)
        cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))

        producto_existente = cursor.fetchone()

        if not producto_existente:
            return {
                "message": "Producto a actualizar no existe"
            },404

        # Ahora obtenemos la data proveniente del body
        data = request.get_json()

        # EL UPDATE SIEMPRE DEBE TENER UN WHERE
        cursor.execute("UPDATE productos SET nombre = %s, precio= %s, cantidad = %s WHERE id = %s RETURNING *",(
            data.get("nombre"),
            data.get("precio"),
            data.get("cantidad"),
            id
        ))

        # En MSSQL primero obtenemos la data y luego hacemos commit sino nos retornara data nula

        # Guardamos los cambios en la base de datos de manera permanente
        conexion.commit()

        # Obtenemos la info actualizada
        producto_actualizado = cursor.fetchone()

        cursor.close()

        return {
            "message":"Producto actualizado exitosamente",
            "content": producto_actualizado 
        }

    elif request.method =='DELETE':
        conexion.rollback()
        cursor = conexion.cursor(row_factory=dict_row)

        cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))
        producto_existente = cursor.fetchone()

        if not producto_existente:
            return {
                "message":"Producto no encontrado"
            }, 404

        cursor.execute("DELETE FROM productos WHERE id = %s", (id,))

        conexion.commit()

        return {
            "message": "Producto eliminado"
        }


# QUERY PARAMS
# parametros enviados por la URL en el cual el cliente pone el nombre de parametro y su valor, esto generalmente se usa para metodos GET porque en los GET JAMAS se envia BODY
@app.route('/buscar-producto')
def buscar_producto():
    print(request.args)

    return {
        "content": []
    }



# ESTO SIEMPRE VA AL FINAL!!!!!
if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    # debug significa que con cada cambio que guardemos los archivos automaticamente se reiniciara el servidor
    app.run(port=5000, debug=True)