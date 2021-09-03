class Coche():
    ruedas=4            #propiedades/caracteristicas
    largoChasis=260
    anchoChasis=130
    arrancado=False

    def arrancar(self): #comportamiento/metodo 
        self.arrancado=True

    def estadoCoche(self):

        if (self.arrancado):
            return "El coche esta funcionando"

        else:
            return "El coche esta parado"

       

mazda=Coche() #ejemplar de clase
renault=Coche()  #ejemplar de clase

print("Mazda tiene: " + str(mazda.ruedas) + " ruedas")
print(mazda.anchoChasis)
print(mazda.largoChasis)
print(mazda.estadoCoche())
print("Renault tiene: " + str(renault.ruedas) + " ruedas")
renault.arrancar()
print("Reanult " + renault.estadoCoche())