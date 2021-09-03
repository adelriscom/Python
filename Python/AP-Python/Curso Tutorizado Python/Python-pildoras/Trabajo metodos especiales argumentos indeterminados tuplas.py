class Persona():

    alamacen_datos=[]

    def __init__(self, *datos): #datos es una tupla, el * es el que me da esa indicación

        for dato in datos:

            self.alamacen_datos.append(dato)
        self.getDatos(self.alamacen_datos)

    def getDatos(self, info):

        for dato in info:
            print(dato)
    
    #def __str__(self):

        #return "Datos de la persona: \n " + str(self.alamacen_datos[0]) + str(self.apellido) + str(self.edad)


p1=Persona("Alexander", "Del Risco", 44, "Mochila", 1200)

print(p1)