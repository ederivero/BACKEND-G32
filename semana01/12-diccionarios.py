# Coleccion de datos 
# Ordenada por llaves y editable

alumno = {
    "nombre": "Juan",
    "apellido": "Zegarra",
    "curso": "Python",
    "hobbies": ["nadar","programar","trabajar"],
    "edad": 35, # No se recomienda que sea numero ya que se puede dar errores al momento de leer la informacion
    "jubilado": False,
    "padres": {
        "padre": {
            "nombre":"Alberto",
            "apellido":"Zegarra"
        },
        "madre":{
            "nombre":"Lucia",
            "apellido":"Hinojosa"
        }
    }
}

print(alumno["nombre"])
# Si quiero acceder de forma "Segura" a una de mis llaves
# si no existe esa llave retornara None (Vacio) o el valor que le pongamos como segundo parametro
print(alumno.get("Nombre","No existe"))

print(alumno.get('nacionalidad'))

# retorna todas las llaves del diccionario
print(alumno.keys())

# retorna todos los valores del diccionario
print(alumno.values())

# Para hacer asignaciones SI O SI usamos los corchetes y no el metodo GET, ese solo es para obtener info
alumno['nacionalidad'] = 'Boliviano'
# alumno.get('nacionalidad') = 'Boliviano'

alumnos = ({'nombre':'juancito'},{'nombre':'martita'}, {'nombre':'robertito'})