import math
#Calculo del área del triángulo usando la formula de herón

#Definición de la funcion

def area_triangulo(mensaje, a, b, c):
    
    #calculo semiperimetro
    s=(a+b+c)/2
    area = math.sqrt(s**(s-a)**(s-b)**(s-c))
    
    return mensaje + str(area)

#lado_a = float(input("Ingrese el primier lado del triangulo, a: "))
#lado_b = float(input("Ingrese el primier lado del triangulo, b: "))
#lado_c = float(input("Ingrese el primier lado del triangulo, c: "))


print(area_triangulo("El area del triangulo es: ", 2, 4, 9))


