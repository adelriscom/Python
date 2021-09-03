edad=int(input("Introduce tu edad, por favor: "))

while edad < 0 or  edad > 80:
    print("Has ingresado una edad no valida")
    edad=int(input("Introduce tu edad, por favor: "))

print("Gracias, puedes pasar")
print("Edad del usuario " + str(edad))