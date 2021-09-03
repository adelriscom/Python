#este programa me permite determinar si un numero es par o impar

#Entradas
numero=int(input("digite un número: "))

#Transformacion
modulo = numero % 2

#Salida

if modulo == 0:
    print("El numero: " + str(numero) + " es par")
    
else:
    print("El numero: " + str(numero) + " es impar")