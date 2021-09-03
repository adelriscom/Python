from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=450)

miFrame.pack()


#miLabel=Label(miFrame, text="Hoy es 4 de Febrero de 2021")
#miLabel.place(x=120, y=125)#esta linea de texto y la anterior se pueden reescribir de la siguiente manera: ver siguiente linea de codigo
#Label(miFrame, text="Esta es otra forma de crear un label").place(x=120, y=125)#de esta forma si quiero modificar mi label seria mas complicado porque no esta en una variable.ACTIVE
miLogo=PhotoImage(file="TechImpeller.png")

Label(miFrame, image=miLogo).place(x=120, y=125)

root.mainloop()
