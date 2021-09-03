class Persona():
    #Propiedades definidas
    nombre=""
    apellido=""
    edad=0
    genero="Sin definir"

    #CONSTRUCTOR establece un estado inicial

    def __init__(self, nombre, apellido, edad, genero):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.genero=genero


    #Métodos/Comportamientos

    def habla(self):

        return "La persona que se llama " + self.nombre + " está hablando"

    def camina(self):

        return "La persona que se llama " + self.nombre + " está caminando"

    def getDatos(self):

        return "Nombre: " + self.nombre + "; Apellido: " + self.apellido + \
            "; Edad: " + str(self.edad) + "; Género: " + self.genero + ";"

        
    
p1 = Persona("Alexander", "Del Risco", 44, "Masculino")

print(p1.getDatos())





