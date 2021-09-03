from io import open

historiaClinica=open("/Users/macintosh/Documents/HistoriasAnonimas/textfrompdf0.txt", "r")

informacion_hc=set()

for linea in historiaClinica.read().split("\n"):
    
    informacion_hc.add(linea)

historiaClinica.close()


print(informacion_hc)
print(len(informacion_hc))
