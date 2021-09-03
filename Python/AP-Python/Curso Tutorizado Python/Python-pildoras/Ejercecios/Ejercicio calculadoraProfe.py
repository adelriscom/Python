from tkinter import *

root=Tk()
miFrame=Frame(root)
miFrame.pack()
operacion=""
resultado=0#esta variable va a acumular los numeros ingresados
coma=False
totalsum=False


digitoDisplay=StringVar()
display=Entry(miFrame, textvariable=digitoDisplay, font="Arial 15")
display.grid(row=1, column=1, columnspan=4, pady=10)
display.config(background="Black", fg="#B0FC38", justify="right", width=30)
digitoDisplay.set("0")

#---------Función alternativa para coma---------------------

def pulsacion_coma():
    
    cont=0
    
    for i in digitoDisplay.get():
        
        if i ==".":
            cont+=1
    if cont==0:
        digitoDisplay.set(digitoDisplay.get() + ".")

#-----------------Pulsaciones numeros-----------------------

def pulsacionesTeclas(numeroPulsado):
    global operacion
    global coma
    
    
    if(operacion!=""):
        
        digitoDisplay.set(numeroPulsado)
        operacion=""
            
    else:
        if(numeroPulsado=="0" and digitoDisplay.get()=="0"):
            digitoDisplay.set("0")
        elif numeroPulsado=="." and digitoDisplay.get()=="0":
            digitoDisplay.set(digitoDisplay.get() + numeroPulsado)
            
        elif numeroPulsado!="0" and digitoDisplay.get()=="0":
            digitoDisplay.set(numeroPulsado)
        
        else:
            digitoDisplay.set(digitoDisplay.get() + numeroPulsado)
    
#----------------funcion suma-----------------------------
    #se pasa por parametro num a la funcion suma
def suma(num):
    #global hace referencia a que se esta utilizando la variable "operacion" que se declaró globalmente
    global operacion
    global resultado
    
    resultado+=float(num)
    
    if resultado.is_integer():
        digitoDisplay.set(int(resultado))
        operacion="suma"
    else:
        operacion="suma"
        digitoDisplay.set(resultado)
#--------------funcion total----------------------

def total():
    
    global resultado
    
    if(resultado + float(digitoDisplay.get())).is_integer():
        digitoDisplay.set(int(resultado + float(digitoDisplay.get())))
        resultado=0
        
    else:
        digitoDisplay.set(resultado + float(digitoDisplay.get()))
        resultado=0  
        
#------------Primera Fila-----------------------#
boton7=Button(miFrame, text="7", width=4, comman=lambda:pulsacionesTeclas("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=4, comman=lambda:pulsacionesTeclas("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=4, comman=lambda:pulsacionesTeclas("9"))
boton9.grid(row=2, column=3)
botondiv=Button(miFrame, text="/")
botondiv.grid(row=2, column=4)

#------------Segunda Fila-----------------------#
boton4=Button(miFrame, text="4", width=4, comman=lambda:pulsacionesTeclas("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=4, comman=lambda:pulsacionesTeclas("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=4, comman=lambda:pulsacionesTeclas("6"))
boton6.grid(row=3, column=3)
botonmult=Button(miFrame, text="*")
botonmult.grid(row=3, column=4)

#------------Tercera Fila-----------------------#
boton1=Button(miFrame, text="1", width=4, comman=lambda:pulsacionesTeclas("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=4, comman=lambda:pulsacionesTeclas("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=4, comman=lambda:pulsacionesTeclas("3"))
boton3.grid(row=4, column=3)
botonrest=Button(miFrame, text="-")
botonrest.grid(row=4, column=4)

#------------Cuarta Fila-----------------------#
boton0=Button(miFrame, text="0", width=4, comman=lambda:pulsacionesTeclas("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=".", width=4, comman=lambda:pulsacion_coma())
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", comman=lambda:total())
botonIgual.grid(row=5, column=3)
botonsum=Button(miFrame, text="+", comman=lambda:suma(digitoDisplay.get()))
botonsum.grid(row=5, column=4)



root.mainloop()