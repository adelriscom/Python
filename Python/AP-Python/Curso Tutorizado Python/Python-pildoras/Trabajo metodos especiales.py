class Persona():

    def __init__(self, nombre, apellido, edad):

        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def __str__(self):

        return "Datos de la persona: \n " + "Nombre: " + self.nombre + " \n Apellido: " + self.apellido + " \n Edad: " + str(self.edad)


p1=Persona("Alexander", "Del Risco", 44)

print(p1)