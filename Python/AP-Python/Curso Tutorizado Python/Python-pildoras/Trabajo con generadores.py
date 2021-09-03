#Primero se define una funcion normal para crear una lista con 6 numeros pares
def generarPares(limite):

    num = 1
    numerosPares = []

    while num < limite:
        numerosPares.append(num*2)

        num=num+1

    return numerosPares


print(generarPares(6))

#Ahora se muestra como se haria con un generador

def generarPares2(limite):

    num = 1
    
    while num < limite:
        
        yield num*2
        num = num+1
    
sucesionPares=generarPares2(6) #objeto iterable sucesionPares

    #Con la estructura for puedo recorrer el objeto iterable es decir sucesionPares

#for i in sucesionPares:
    #print(i)

#En lugar de utilizar una estructura "for" se puede utilizar 
# uno de los metodos que tiene un generador para ver el siguiente valor
#en este caso utilizamos el metodo "next"

print(next(sucesionPares))
print("Ahora va  siguiente valor: ")
print(next(sucesionPares))

#En esta seccion se trabaja con la estructura "yield from" 
#la cual tiene como utilidad simplificar el codigo de los
#generadores en el caso de utilizar bucles anidados

def capitales_mundo(*ciudades): #El asterisco (*) indica que vamos a pasar un numero indeterminado de parametros y lo tomara como una tupla
    #Este for recorre los elementos pasados 
    # por parametros al generador 
    for capital in ciudades: #con este bucle buscamos el primer elemento
        #for letra_capital in capital: #con este for buscamos los componentes del primer elelmento, es decir las letras de Berlin
           # yield letra_capital #devuelve las letras
        #yield capital #yield nos devuelve cada uno de esos eleentos
        yield from capital # con esta intruccion reemplazamos el for anidado
#capitales_devueltas es nuestro objeto iterable
#a este objeto se le asignan las capitales del mundo
#lo que recibe este objeto es una tupla al haber definido en el 
#generador el asterisco(*) como prte del parametro

capitales_devueltas = capitales_mundo("Berlin", "Roma", "Bogota", "Pekin", "Hanoi")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))