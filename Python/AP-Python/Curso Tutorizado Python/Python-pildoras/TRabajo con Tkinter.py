from tkinter import *

raiz=Tk()#constructor Tk

raiz.title("Mi primera ventana Python")

raiz.resizable()#permite redimensionar la ventana, recibe 2 parametros booleanos 0=False, 1=True

raiz.iconbitmap("/Users/macintosh/Downloads/Icono - logo Bilaboral.ico")
raiz.config(bg="green")

miFrame=Frame()#se crea el frame
miFrame.pack()#se empaqueta el frame

miFrame.config(bg="red")#fondo del frame
miFrame.config(width="650", height="350")#tamaño del frame



raiz.mainloop()#este es un bucle infinito que permite tener la vcentana abierta. esta instruccion debe ser la ultima dentro del codigo de la ventana