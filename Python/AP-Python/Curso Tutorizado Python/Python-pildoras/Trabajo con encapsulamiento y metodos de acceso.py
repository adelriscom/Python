class Persona():
    #Propiedades definidas
    __nombre="" #esta propiedad esta encapsulada. se ha utilizado la doble raya al piso para tal fin
    apellido=""
    __edad=0    #esta propiedad esta encapsulada. se ha utilizado la doble raya al piso para tal fin
    genero="Sin definir"

    #CONSTRUCTOR establece un estado inicial

    def __init__(self, nombre, apellido, genero):
        self.__nombre=nombre
        self.apellido=apellido
        self.genero=genero

    #Definicion del método SETTER

    def setEdad(self, laEdad):

        if(laEdad<0) or (laEdad>100):
            return print("Error en la edad")
        
        else:
            self.__edad=laEdad
            return self.__edad


    #Métodos/Comportamientos

    def habla(self):

        return "La persona que se llama " + self.__nombre + " está hablando"

    def camina(self):

        return "La persona que se llama " + self.__nombre + " está caminando"

    def getDatos(self):

        return "Nombre: " + self.__nombre + "; Apellido: " + self.apellido + \
            "; Edad: " + str(self.__edad) + "; Género: " + self.genero + ";"

        
    
p1 = Persona("Alexander", "Del Risco", "Masculino")
p1.setEdad(200)
print(p1.getDatos())
