from tkinter import *
from tkinter import messagebox as MessageBox
raiz=Tk()

miFrame=Frame(raiz, width=1000, height=550)
miFrame.pack()

#Variables para almacenar texto en los cuadro de texto cuadroTextoXXX

miNombre=StringVar()
miApellido=StringVar()
miContrasena=StringVar()
miEmail=StringVar()
miDireccion=StringVar()
miComentario=StringVar()


#cuando se quiere ubicar varios elementos en la interfaz, conviene utilizar el metodo grid() en lugar de place, esto porque es dificil ubicar dichos elemento con base en las coordenadas
cuadroTextoNombre=Entry(miFrame, textvariable=miNombre)
cuadroTextoNombre.grid(row=0, column=1, padx=8, pady=8)

cuadroTextoApellido=Entry(miFrame, textvariable=miApellido)
cuadroTextoApellido.grid(row=1, column=1, padx=8, pady=8)

cuadroTextoContra=Entry(miFrame, textvariable=miContrasena)
cuadroTextoContra.grid(row=2, column=1, padx=8, pady=8)
cuadroTextoContra.config(show="*")

cuadroTextoEmail=Entry(miFrame, textvariable=miEmail)
cuadroTextoEmail.grid(row=3, column=1, padx=8, pady=8)

cuadroTextoDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroTextoDireccion.grid(row=4, column=1, padx=8, pady=8)

cuadroTextoComentarios=Text(miFrame, width=26, height=5)
cuadroTextoComentarios.grid(row=5, column=1, padx=8, pady=8)

#Estas instrucciones permiten crear el scrollbar vertical del campo comentario
miScrollVertical=Scrollbar(miFrame, command=cuadroTextoComentarios.yview)
miScrollVertical.grid(row=5, column=2, sticky="nsew")
cuadroTextoComentarios.config(yscrollcommand=miScrollVertical.set)
#cuadroTexto.place(x=120, y=110)


nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w")

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w")

emailLabel=Label(miFrame, text="Email: ")
emailLabel.grid(row=3, column=0, sticky="w")

direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=4, column=0, sticky="w")

contraLabel=Label(miFrame, text="Contraseña: ")
contraLabel.grid(row=2, column=0, sticky="w")

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="w")
#nombreLabel.place(x=55, y=110)

def funcionBoton():
    #MessageBox.showinfo("Saludo", "Hola desde Tkinter")
    miNombre.set("Alexander")
    #para establecer texto en el area de comentarios se debe hacer lo siguiente
    
    cuadroTextoComentarios.insert(INSERT, "Mi nombre es Alexander y este texto se establece en comentarios")
    #recupera informacion escrita en el texto
    print(cuadroTextoNombre.get())
    MessageBox.showinfo("Informacion rescatada", cuadroTextoApellido.get())
    
    
    
    
    
    

botonEnviar=Button(raiz, text="Enviar", command=funcionBoton)
botonEnviar.pack()



raiz.mainloop()