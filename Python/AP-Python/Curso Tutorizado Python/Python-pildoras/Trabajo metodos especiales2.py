#import datetime

#hoy=datetime.date.today()

#print(repr(hoy))

class Agenda():

    def __init__(self):

        self.miAgenda={}

    def agregarPersonas(self, nombre, telefono):

        self.miAgenda[nombre]=telefono

    def __len__(self):

        return len(self.miAgenda)


agendaPersonal=Agenda()

agendaPersonal.agregarPersonas("Alexander", "3152987656")
agendaPersonal.agregarPersonas("Marcela", "3187986543")

print(len(agendaPersonal))



#class Persona():

    #def __init__(self, nombre, apellido, edad):

        #self.nombre=nombre
        #self.apellido=apellido
        #self.edad=edad

    #def __str__(self):

        #return "Datos de la persona: \n " + "Nombre: " + self.nombre + " \n Apellido: " + self.apellido + " \n Edad: " + str(self.edad)

    #def __repr__(self):

        #return "Datos de la persona: \n " + "Nombre: " + self.nombre + " \n Apellido: " + self.apellido + " \n Edad: " + str(self.edad)


#p1=Persona("Alexander", "Del Risco", 44)

#print(p1)