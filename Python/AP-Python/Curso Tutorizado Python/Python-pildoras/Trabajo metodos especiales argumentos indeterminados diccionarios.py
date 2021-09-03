class Persona():

    def __init__(self, **datos):

        elementos=datos.items()

        for clave, valor in elementos:

            print(clave, " " , valor)


p1=Persona(Edad=45, AgnoNacimiento=1976, Mes=10, Dia=1, Nombre="Alexander", Apellido="Del Risco")
print("\n")
p2=Persona(Edad=44, AgnoNacimiento=1977, Mes=11, Dia=23, Nombre="Marcela", Apellido="Falla")