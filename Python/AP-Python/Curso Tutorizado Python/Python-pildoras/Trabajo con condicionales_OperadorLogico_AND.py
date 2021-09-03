print("Obtencion de licencia de conduccion")

edad=int(input("Introduce tu edad, por favor: "))

vision=input("Tienes la vision correcta? ")

if edad >= 18 and edad < 90 and vision=="si":
    print("Puedes intentar obtener la licencia")

else:
    print("Lo siento. No cumples los requisitos")