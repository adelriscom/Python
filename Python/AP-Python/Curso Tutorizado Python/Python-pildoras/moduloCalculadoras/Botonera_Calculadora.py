from tkinter import*

from moduloCalculadoras.Operaciones_Calculadora import*


#contador=0
        
def construir_botones(self, botones, filas_botones):
    contador=0        

#For para recorrer filas y for anidado para recorrer columnas
        
    for fila in range(2, filas_botones+2):
        for columna in range(4):
            botones[contador].grid(row=fila, column=columna)
            contador+=1
    
    #Definicion de la función colocar_Boton, se pasan dos parametros, valor y mostrar, al asignar un valor buleano al parametro mostrar hace que ese parametro sea opcional ya que algunos botones no tienen esa propiedad           
def colocar_Boton(self, valor, mostrar=True, ancho=9, alto=1):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 9), command=lambda:pulsaciones_teclas(self, valor, mostrar))