# En python tambien se pueden pasar n parametros con el nombre del parametro usando los **kwargs (keyword argunments)
def crear_perfil(id, **datos):
    # Se necesita enviar un correo de bienvenida si a la funcion se le pasa el parametro correo o email
    print(id)
    print(datos)

crear_perfil(id=1, nombre="Eduardo",edad=30)
crear_perfil(id=2, nombre="Valeria",nacionalidad="Peruana",estado_civil="Viuda")