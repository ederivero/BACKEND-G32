# Coleccion de datos Editable pero no es ordenada
# Se suelen utilizar para almacenar informacion y luego corroborar su contenido sin importar algun orden en especifico
roles = {"USUARIO", "ADMIN", "INVITADO", "ALUMNO", "PROFESOR"}
print(roles)

# No es posible acceder a un conjunto por su posicion
# print(roles[1])

# Asi se agrega nuevos datos a mi conjunto
roles.add("SUPERADMIN")

# Asi se elimina los datos del conjunto
roles.remove("USUARIO")
roles.add("SUPERADMIN")

# Los conjuntos (SET) se usan para poder evitar duplicidad de informacion, es decir, si se intenta agregar el mismo valor mas de una vez lo omitira, esto es sensible a Mayus y Minus

# not in > no esta
# in > esta
# is > es / ser
print("COORDINADOR" in roles)
print("ALUMNO" in roles)