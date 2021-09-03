

import random
import clasificacionRecipientes
#------------------------------------

#Programa

listVolRecip = [60, 100, 200, 250, 300, 600, 1001]
resultado = clasificacionRecipientes.clasificacion_recipientes(listVolRecip)
print("\nLa lista del volumen de los recipientes: " , listVolRecip)
print("Resultado de la clasificacion de recipientes: ", resultado)

listVolRecip = list()
print("\nLa lista del volumen de los recipientes: " , listVolRecip)
print("Resultado de la clasificacion de recipientes: ")
print(clasificacionRecipientes.clasificacion_recipientes(listVolRecip))

#Lista generada con numeros aleatorios con numeros enteros

listVolRecip = list()
for i in range(100000):
    numAleat = random.randint(10, 2000)
    listVolRecip.append(numAleat)
    
print("\nLa lista del volumen de los recipientes con numeros enteros: " , listVolRecip)
print("Resultado de la clasificacion de recipientes: ")
print(clasificacionRecipientes.clasificacion_recipientes(listVolRecip))

#Lista generada con numeros aleatorios con numero decimales

listVolRecip = list()
for i in range(100000):
    numAleat = round(random.uniform(10, 2000), 2)
    listVolRecip.append(numAleat)
    
print("\nLa lista del volumen de los recipientes con numeros decimales: " , listVolRecip)
print("Resultado de la clasificacion de recipientes: ")
print(clasificacionRecipientes.clasificacion_recipientes(listVolRecip))