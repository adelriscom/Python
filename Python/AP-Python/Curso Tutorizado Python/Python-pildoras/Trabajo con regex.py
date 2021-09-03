import re

cadena="Estoy trabajando con python en domingo y es semana santa. El próximo domingo no pienso grabar ningun video"

busqueda="domingo"

#con este codigo se busca la palabra domingo dentro del texto definido en la variable cadena
'''if re.search(busqueda, cadena) is not None:
    print("Se encontró el termino", busqueda)
    
else:
    print("No se encontró el término", busqueda)'''
    
#codigo para ver en donde se encuentra el texto buscado

texto_encontrado = re.search(busqueda, cadena)

'''print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())'''

print(re.findall(busqueda, cadena))
print(len(re.findall(busqueda, cadena)))