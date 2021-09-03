import re

lista_nombres = ["Antonio Banderas", "Salma Hayek", "Tomás Cruceros", "Antonio Resines", "Friedrich Hayek"]

lista_nombres2 = ["http://www.pildorasinformaticas.es", "ftp://www.pildorasinformaticas.es", "http://www.pildorasinformaticas.com", "ftp://www.pildorasinformaticas.com"]

lista_terminos = ["camión", "camion", "niñas", "niños", "ejemplo"]

#Buscar cadenas que comiencien con el nombre Antonio
for nombre in lista_nombres:
    if re.findall("^Antonio", nombre):
        print(nombre)


#Buscar cadenas que terminen con el apellido Hayek
for nombre in lista_nombres:
    if re.findall("Hayek$", nombre):
        print(nombre)
        
##Buscar cadenas que terminen con una cadena especifica
for nombre in lista_nombres2:
    if re.findall(".es$", nombre):
        print(nombre)
        
##Buscar cadenas que comiencen con una cadena especifica
for nombre in lista_nombres2:
    if re.findall("^ftp", nombre):
        print(nombre)
        

##Buscar cadenas con el metacaracter [
for termino in lista_terminos:
    if re.findall("cami[oó]n", termino):
        print(termino)
        
##Buscar cadenas con el metacaracter [
for termino in lista_terminos:
    if re.findall("niñ[oa]s", termino):
        print(termino)