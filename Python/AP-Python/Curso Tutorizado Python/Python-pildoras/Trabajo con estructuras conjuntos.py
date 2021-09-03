sistema_solar="Mercurio Venus Tierra Marte Jupiter Saturno Urano Neptuno Pluton"

planetas=set()
#planetas=set(sistema_solar)#si se establece la variable sistema_solar como parametro del metodo set, se evaluan los elemento que contien el string, es decir las letras y demas elementos que contiene ese string

for planeta in sistema_solar.split(" "):#Se esta indicando que cada elemento esta separado por un espacio en blanco
    
    planetas.add(planeta)
    
print(planetas)
print(len(planetas))
    
    
    
    
    
