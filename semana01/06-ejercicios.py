# 1. Ingresa por teclado el monto a pagar y que me imprima por consola el monto de propina que debo de dar siendo el 10%
monto = int(input('Ingresa el monto a pagar: '))
propina = monto * 0.10
print(f'La propina que debes dar es: {propina}')

# 2. Dado un total de segundos (3746), Calcula cuantas horas, minutos y segundos representan usando los operadores aritmeticos // y %
segundos = 3746
horas = segundos // 3600 # 1 hora : 3600 segundos
minutos = (segundos - (horas * 3600)) // 60  # 1 hora : 60 minutos
total_segundos = segundos - (minutos * 60 + horas * 3600)
print(f'{segundos} segundos es {horas} horas con {minutos} minutos y {total_segundos} segundos')
# 1h con 2 minutos y 26 seg

# 3. Ingresa un numero y quiero que me diga si es PAR o IMPAR (use el operador aritmetico %)
numero = int(input('Ingresa un numero: '))
resultado = numero % 2
print(f'El numero es {resultado}')

# 4. Ingresa un monto por teclado y luego haga lo siguiente: 1. aumente 250, luego retire 400 y luego genere un cobro de interes del 5% (multiplicar por 1.05)
monto = int(input('Ingresa el monto: '))
resultado = monto + 250 - 400
interes = resultado * 1.05
print(f'El total a pagar es {interes}')