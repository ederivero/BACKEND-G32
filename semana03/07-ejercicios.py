# 1. Crear un sistema para calcular sueldos de distintos tipos de empleados
# Clase base Empleado
# atributos: nombre (publico) y sueldo_base (privado)
# crear su getter y setter para el sueldo_base (el setter no debe permitir valores negativos)
# metodo calcular_sueldo() que retorna el sueldo_base
# mostrar_info() imprime el nombre y el sueldo calculado

# Clase hijas
# EmpleadoVentas y su atributo comision (monto fijo) y sobreescribir calcular_sueldo() para que retorne el sueldo_base + comision
# EmpleadoTiempoParcial y sus atributos horas_trabajadas y pago_por_hora y sobreescribir calcular_sueldo() para que retorne el horas_trabajas * pago_por_hora e ignora el sueldo base

# Para validar: 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Calcular e imprimir el total de la planilla (suma de todos los sueldos de los empleados)

# --------------------------------------

# 2. Crear un sistema de inventario simple
# Clase base Producto
# atributos: nombre, precio(privado) y stock
# crear getter y setter para el precio (no negativos)
# metodo calcular_precio_final() que por defecto retorna el precio sin cambios
# metodo vender(cantidad) que resta del stock si hay suficiente, sino, muestra un mensaje de error y no resta stock

# Clases hijas
# ProductoConDescuento: atributo porcentaje_descuento. sobreescribir calcular_precio_final() aplicar el dscto sobre el precio
# ProductoImportado: atributo impuesto_aduanero (porcentaje). sobreescribir calcular_precio_final() para sumar ese impuesto al precio

# Para validar 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Intentar asignar un precio negativo a alguno de ellos usando el setter y comprobar el mensaje de error
