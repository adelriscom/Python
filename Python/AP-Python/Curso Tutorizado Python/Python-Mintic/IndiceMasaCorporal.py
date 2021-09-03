
#Definicion de variables: Peso y estatura

#peso=float(input("Ingrese el peso: "))
#altura=float(input("Ingrese la altura: "))

peso=float(input())
altura=float(input())

#transformar altura
cuadradoAltura=round(altura**altura, 0)
#print(cuadradoAltura)

#Calcular Indice de masa corporal IMC
#imc variable donde se almacena valor calculado

imc=round(peso/cuadradoAltura, 0)
#print(imc)
#Salida: se imprime el valor calculado de imc

#print("El indice me masa corporal es: " + str(imc))


if imc<18.5:
    print("Bajo peso")

elif imc>=18.5 and imc<24.9:
    print("Normal")

elif imc>=25.0 and imc<29.9:
    print("Sobrepeso")

else:
    print("Obeso")
    