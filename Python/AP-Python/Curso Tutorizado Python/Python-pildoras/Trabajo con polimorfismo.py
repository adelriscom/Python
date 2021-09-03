class persona():

    def hablar(self):
        return "Hablo como persona"

class Trabajador(persona):

    def hablar(self):
        return "Hablo como un trabajador"

class Director(Trabajador):

    def hablar(self):
        return "Hablo como un director"

def hazlesHablar(listaDeLasPersonas):

    for persona in listaDeLasPersonas:

        print(persona.hablar())

Antonio=persona()
Maria=Trabajador()
Ana=Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("--------------------------------------------------------")

listaPersonas=[Antonio, Ana, Maria]

hazlesHablar(listaPersonas)
