

paises = {}
#ciudades = []
mensaje = "salir"
salida = " "

while mensaje != salida:

    pais = input("Ingrese el pais: ")

    if pais == "salir":
        salida = mensaje
     
    if pais != "salir":
        ciudad = input("Ingrese la ciudad: ")        
        ciudades = paises.setdefault(pais, [ciudad])
    if ciudades != [ciudad]:
        paises[pais].append(ciudad)

print(paises)


