import re


lista_terminos = ["camión", "camion", "niñas", "niños", "ejemplo"]
print("-----------------------------------------------------------")
print("Buscar cadenas en un rango de letras en el rango [p-z]")
print("-----------------------------------------------------------")
#Buscar cadenas en un rango de letras
for termino in lista_terminos:
    if re.findall("[p-z]", termino):
        print(termino)

print("-----------------------------------------------------------")
print("Buscar cadenas en un rango de letras que comiencen con un termino o letra en el rango [a-f]")
print("-----------------------------------------------------------")
#Buscar cadenas en un rango de letras que comiencen con un termino o letra
for termino in lista_terminos:
    if re.findall("^[a-f]", termino):
        print(termino)
        
print("-----------------------------------------------------------")
print("Buscar cadenas en un rango de letras que terminen con un termino o letra en el rango [l-p]")
print("-----------------------------------------------------------")
#Buscar cadenas en un rango de letras que comiencen con un termino o letra
for termino in lista_terminos:
    if re.findall("[l-p]$", termino):
        print(termino)
        
print("-----------------------------------------------------------")
print("Fin del ejercicio")
print("-----------------------------------------------------------")