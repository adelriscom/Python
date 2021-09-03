import random
import moduloReto4ClasifiHuevos
#------------------------------------

#Programa

tamHuevo = [60, 100, 200, 250, 300, 600, 1001]
resultado = moduloReto4ClasifiHuevos.clasificacion_huevos(tamHuevo)
print("\nLa lista del volumen de los recipientes: " , tamHuevo)
print("Resultado de la clasificacion de recipientes: ", resultado)

tamHuevo = list()
print("\nLa lista del volumen de los recipientes: " , tamHuevo)
print("Resultado de la clasificacion de recipientes: ")
print(moduloReto4ClasifiHuevos.clasificacion_huevos(tamHuevo))

#Lista generada con numeros aleatorios con numeros enteros

tamHuevo = list()
for i in range(100000):
    numAleat = random.randint(10, 2000)
    tamHuevo.append(numAleat)
    
print("\nLa lista del volumen de los recipientes con numeros enteros: " , tamHuevo)
print("Resultado de la clasificacion de recipientes: ")
print(moduloReto4ClasifiHuevos.clasificacion_huevos(tamHuevo))

#Lista generada con numeros aleatorios con numero decimales

tamHuevo = list()
for i in range(100000):
    numAleat = round(random.uniform(10, 2000), 2)
    tamHuevo.append(numAleat)
    
print("\nLa lista del volumen de los recipientes con numeros decimales: " , tamHuevo)
print("Resultado de la clasificacion de recipientes: ")
print(moduloReto4ClasifiHuevos.clasificacion_huevos(tamHuevo))