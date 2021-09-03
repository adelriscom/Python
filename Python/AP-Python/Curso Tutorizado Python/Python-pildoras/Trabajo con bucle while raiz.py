import math

print("Vamos a encontrar la raiz cuadrada de un numero")

num=int(input("ingrese un numero positivo, por favor: "))

intentos = 1

while num < 0:
    print("No se puede hallar la raiz cuadrada de un numero negativo")
    num=int(input("ingrese un numero, por favor: "))

    intentos= intentos+1

    if intentos == 5:

        break

if intentos == 5:
    print("Ingresó un numero negativo muchas veces, por lo tanto no se puede hallar la raiz cuadrada")

else:
    raiz=math.isqrt(num)
    print("El numero ingresado es: " + str(num) + " la raiz cuadrada es: " + str(raiz))