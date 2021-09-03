class Vehiculo():

    def __init__(self, color, ruedas, ancho, alto, marchas):

        self.color=color 
        self.ruedas=ruedas
        self.ancho=ancho
        self.alto=alto
        self.marchas=marchas
        self.arrancando=False
        self.frenando=False
        self.girando=False

    def Arrancar(self):

        self.arrancando=True

    def Frenar(self):

        self.frenando=True

    def Girar(self):

        self.girando=True

class Coche(Vehiculo):

    def __init__(self, color, ruedas, ancho, alto, marchas, cilindrada, asientos, aire_acondicionado):
        super().__init__(color, ruedas, ancho, alto, marchas)

        self.cilindrada=cilindrada
        self.asientos=asientos
        self.aire_acondicionado=aire_acondicionado

    def Ir_Marcha_Atras(self):

        self.marcha_Atras=True

    def Arrancar(self):

        self.arrancar=True

class Furgoneta(Coche):

    def __init__(self, color, ruedas, ancho, alto, marchas, cilindrada, asientos, aire_acondicionado, carga):
        super().__init__(color, ruedas, ancho, alto, marchas, cilindrada, asientos, aire_acondicionado)

        self.carga=carga

    def Cargar(self):

        self.cargando=True

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, ancho, alto, marchas):

        super(). __init__(color, ruedas, ancho, alto, marchas)

    def Saltar(self):

        self.saltando=True

    def Derrapar(self):

        self.derrapando=True

class Moto(Coche, Bicicleta):

    def __init__(self, color, ruedas, ancho, alto, marchas, cilindrada, asientos):

        super().__init__(self, color, ruedas, ancho, alto, marchas, cilindrada, asientos)
        #Bicicleta.__init__(self, color, ruedas, ancho, alto, marchas)




