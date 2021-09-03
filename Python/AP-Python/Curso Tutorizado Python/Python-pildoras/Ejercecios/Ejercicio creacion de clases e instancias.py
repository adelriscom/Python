#Creacion de clase
class CuentaCorriente():

    #Definición de atributos
    numeroCuenta=""
    titularCuenta=""
    saldoCuenta=0
    consignacion=0
    retiroCuenta=0
    nuevoSaldoR=0
    nuevoSaldoC=0
    #bonus_promocion=0

    #Definición constructor

    def __init__(self, cuenta, titular, saldo):
        self.numeroCuenta=cuenta
        self.titularCuenta=titular
        self.saldoCuenta=saldo

    #Definición de Metodos

    def ingresarDinero(self):
        
        consignacion=int(input("Ingrese la cantidad a consignar: "))
        print("Ud. ha consignado: " + str(consignacion))
        self.nuevoSaldoC=self.saldoCuenta + consignacion

        return print("Este es su nuevo saldo: " + str(self.nuevoSaldoC))
        
    def retirarDinero(self):

        try:
            retiroCuenta=int(input("Cuanto dinero quiere retirar: "))
            self.nuevoSaldoR=self.nuevoSaldoC-retiroCuenta

            if (self.nuevoSaldoR<0):
                          
                self.nuevoSaldoR=self.nuevoSaldoC          
                raise ValueError
                #print("Ud. no tiene saldo suficiente para realizar el retiro")

            else:

                print("Ud. ha retirado: " + str(retiroCuenta))
                
        
        except ValueError:

            print("Ud. no tiene saldo suficiente para realizar el retiro")

        return print("Su saldo es: " + str(self.nuevoSaldoR))
            
        

    def getDatosBancarios(self):

        return "Numero de cuenta: " + self.numeroCuenta + "; Titular: " + self.titularCuenta + "; Saldo inicial de la cuenta: " + str(self.saldoCuenta) + \
            "; Saldo cuenta despues de consignación: " + str(self.nuevoSaldoC) + "; Saldo cuentas despues de retiro: " + str(self.nuevoSaldoR)




class CuentaJoven(CuentaCorriente):

    def __init__(self, cuenta, titular, saldo, bono):
        
        super().__init__(cuenta, titular, saldo)

        self.bonus_promocion = bono
        self.nuevoSaldoC=self.saldoCuenta + self.bonus_promocion

    def getBonus(self):

        return "El bonus fue por: " + str(self.bonus_promocion)

    def ingresarDinero(self):

        return super().ingresarDinero()

    def retirarDinero(self):

        return super().retirarDinero()

    def getDatosBancarios(self):

        return super().getDatosBancarios() + " Bono: " + str(self.bonus_promocion)


miCuenta=CuentaCorriente("235689", "Alexander Del Risco", 200)
miCuentaJoven=CuentaJoven("546589", "Pedro Gomez", 600, 200)

miCuenta.ingresarDinero()
miCuenta.retirarDinero()


miCuentaJoven.ingresarDinero()
miCuentaJoven.retirarDinero()


#print(miCuenta.getDatosBancarios())

print(miCuentaJoven.getDatosBancarios())
