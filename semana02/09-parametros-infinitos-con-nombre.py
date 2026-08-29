# En python tambien se pueden pasar n parametros con el nombre del parametro usando los **kwargs (keyword argunments)
def crear_perfil(id, **datos):
    # el kwargs se almacena en formato de un diccionario
    # Se necesita enviar un correo de bienvenida si a la funcion se le pasa el parametro correo o email
    if datos.get("correo") or datos.get("email"):
        print("Se envio el correo de bienvenida")
    else:
        print("No se envio el correo")
    print(id)
    print(datos)

crear_perfil(id=1, nombre="Eduardo",edad=30)
crear_perfil(id=2, nombre="Valeria",nacionalidad="Peruana",estado_civil="Viuda", email="val123@hotmail.com")

# Se puede combinar los *args con los **kwargs pero siguiendo el orden de primero los args y luego los kwargs
def registrar_alumno(nombre, *cursos, **datos_extra):
    print(f"Alumno {nombre}")

    print("Cursos inscritos")
    for curso in cursos:
        print(f"* {curso}")

    print("Datos adicionales:")
    for clave, valor in datos_extra.items():
        print(f"* {clave}: {valor}")

registrar_alumno("Eduardo","Python","Flask","Django", 
                 edad=30, 
                 ciudad="Arequipa", 
                 hobbies=["Nada","Enseñar", "Jugar"])


# Crear una funcion calcular_total que reciba cualquier cantidad de montos (numeros) y un parametro con el nombre moneda (kwargs) con el valor de la divisa, por defecto sera USD sino se envia nada
def calcular_total(*montos, **otros_valores):
    total = 0
    for monto in montos:
        total += monto
    # .get como segundo parametro se le puede pasar un valor por defecto
    divisa = otros_valores.get("moneda", "USD")
    print(f"Total: {total}{divisa}")

calcular_total(100,250,500,moneda="PEN")
calcular_total(200,500,1000)