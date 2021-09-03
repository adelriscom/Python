import random

cont = 0
aleatorio = random.randint(1,100)
numero = 0

while numero != aleatorio:
    numero = int(input("ingrese un numero entre 1 y 100: "))

    if numero < aleatorio:
        print("el numero aleatorio es mayor")
        
    elif numero > aleatorio:
        print("El numero aleatorio es menor")
    
    else:
        print("el numero aleatorio es igual al numero ingresado")

    cont = cont + 1

print("El numero ingresado es: " + str(numero) + " Y el numero aleatorio es: " + str(aleatorio))
print("Has relizado: " + str(cont) + " Intentos")
    