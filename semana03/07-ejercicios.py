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

class Empleado:
	def __init__(self, nombre):
		self.nombre = nombre
		self.__sueldo_base = None

	@property
	def sueldo_base(self):
		return self.__sueldo_base

	@sueldo_base.setter
	def sueldo_base(self, nuevo_sueldo_base):
		if nuevo_sueldo_base < 0:
			print(f"Error: No puede tener sueldo base negativo")
			return

		self.__sueldo_base = nuevo_sueldo_base

	def calcular_sueldo(self):
		return self.sueldo_base
	

	def mostrar_info(self):
		print(f"Empleado: {self.nombre} | Sueldo : {self.__sueldo_base}")


class EmpleadoVentas(Empleado):
	def __init__(self, nombre, comision):
		super().__init__(nombre)
		self.comision = comision

	def calcular_sueldo(self):
		return self.sueldo_base + self.comision

	def mostrar_info(self):
			print(f"Empleado: {self.nombre} | Sueldo : {self.calcular_sueldo()}")

class EmpleadoTiempoParcial(Empleado):
	def __init__(self, nombre, horas_trabajadas, pago_por_hora):
		super().__init__(nombre)
		self.horas_trabajadas = horas_trabajadas
		self.pago_por_hora = pago_por_hora

	def calcular_sueldo(self):
		return self.horas_trabajadas * self.pago_por_hora

	def mostrar_info(self):
				print(f"Empleado: {self.nombre} | Sueldo : {self.calcular_sueldo()}")

empleados = [Empleado("Eduardo"), EmpleadoVentas("Anita",300), EmpleadoTiempoParcial("Roxana",80, 20)]

planilla = 0
for emp in empleados:
	emp.sueldo_base= 1500
	emp.mostrar_info()

	planilla += emp.calcular_sueldo()

print(f"TOTAL DE LA PLANILLA : {planilla:.2f}")

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
class Producto:
	def __init__(self, nombre, stock):
		self.nombre = nombre
		self.__precio = None
		self.stock = stock

	@property
	def precio(self):
		 return self.__precio

	@precio.setter
	def precio(self, nuevo_precio):
		if nuevo_precio < 0:
			print(f"Error: El precio no puede ser negativo")
			return

		self.__precio = nuevo_precio

	def calcular_precio_final(self):
		return self.__precio

	def vender(self, cantidad):
		if cantidad <= self.stock:
			print(f"Venta Exitosa!")
		else:
			print(f"Error: La venta no puede ser porque no hay stock del producto")

class ProductoConDescuento(Producto):
	def __init__(self,nombre, stock, porcentaje_descuento):
		super().__init__(nombre,stock)
		self.porcentaje_descuento = porcentaje_descuento

	def calcular_precio_final(self):
		descuento = self.precio * (self.porcentaje_descuento / 100)
		return self.precio - descuento


class ProductoImportado(Producto):
	def __init__(self,nombre,stock, impuesto_aduanero):
		super().__init__(nombre,stock)
		self.impuesto_aduanero = impuesto_aduanero

	def calcular_precio_final(self):
		impuesto = self.precio * (self.impuesto_aduanero / 100)
		return self.precio + impuesto



productos = [Producto("Cuaderno",5), ProductoConDescuento("Mochila",20,15), ProductoImportado("Laptop", 300, 18)]

productos[0].precio = -1

for producto in productos:
	producto.precio = 500


productos[0].vender(10) # Imprimir venta invalida
productos[1].vender(5) # Venta valida
productos[2].vender(1) # Venta valida