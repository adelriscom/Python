#lasCapitales= {"Espan":"Madrid", "Francia":"Paris", "Reino Unido":"Londres"}

#Agregar un elemento al diccionario
#lasCapitales["Colombia"]="Bogota"

#print(lasCapitales)

#Eliminar un elemento del diccionario
#del lasCapitales["Reino Unido"]
#print(lasCapitales)

#datos={"Espana":"Madrid",23:"Michael Jordan", "Mosqueteros":3}
#print(datos)

#Usando tuplas que despues se utilizan en una estructura diccionario: clave valor
#claveCapitales=["Espan", "Reino Unido", "Colombia", "Portugal"]
#capitalesMundo={claveCapitales[0]:"Madrid", claveCapitales[1]:"Londres", claveCapitales[2]:"Bogota", claveCapitales[3]:"Lisboa"}
#print(capitalesMundo)

#Acceder a un elemento de un diccionario mediante la clave
#print(capitalesMundo["Colombia"])

#Acceder a un elemento de un diccionario sin conocer la clave
#print(capitalesMundo.keys())
#print(capitalesMundo.values())
#print(len(capitalesMundo))

#Diccionarios anidados

#datosJordan={23:"Jordan","Nombre":"Michael","Equipo":"C Bulls","anillos":[1991,1992,1993,1996,1997,1998]}
#print(datosJordan["anillos"])

#ejemDiccionario={"Clave1":234,"Clave2":True,"Clave3":"Valor1","Clave4":[1,2,3,4]}

#print(ejemDiccionario)
#type(ejemDiccionario)

#print(ejemDiccionario["Clave1"])

#versiones = {'python': 2.7, 'zope': 2.13, 'plone': None}
#print(versiones["plone"])
#versiones["plone"]=5.1
#print(versiones)

#print("plone" in versiones)

versiones = {"python":2.7, "zope":2.13, "plone":5.1}
zope = versiones.setdefault("zope")
print ('Versiones instaladas:', versiones)
