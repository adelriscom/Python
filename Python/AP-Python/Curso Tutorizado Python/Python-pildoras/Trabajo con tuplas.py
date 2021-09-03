#Definimos una tupla
misDatos=("Alexander", 43, 1, 10, 1976)
print(misDatos)

#convertir tupla en lista
misDatosLista=list(misDatos)
print(misDatosLista)

#Definimos una lista para convertirla en tupla
otrosDatos = ["Marcela", 42, 23, 11, 1977]
otrosDatosTupla= tuple(otrosDatos)
print(otrosDatosTupla)

#Buscar un elemento enla tupla
print("Marcela" in otrosDatosTupla)
print("Marcela" in misDatos)

#Desempaquetar una tupla
nombre, agnos, dia, mes, agno=misDatos
print(nombre)