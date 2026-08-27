# bucle (infinito) que se repetira hasta que la condicion no se cumpla

contador = 0
# while > mientras
while contador < 10:
    print("Hola")
    contador += 1

print("Adios")

print ('--------')
# en los bucles (while y for) podemos terminar la iteracion de manera anticipada con el break
contador = 0
while contador < 100:
    print(contador)
    if contador == 10:
        break
    contador += 1

# continue > salta esa iteracion
print ('--------')
contador = 0
while contador < 10:
    contador += 1
    if contador == 7:
        continue
    print(contador)



print ('--------')
# En el while se puede agregar un else y se ingresara cuando el while termine
numero = 5 
while numero > 0:
    print(numero)
    numero -= 1
else:
    print("ACABOOOO")