

def calcularProm(notasEstud, materia):
    
    #notasEstud = "Hugo,3,4,5;Paco,2,5;Luis,5,4,3,2"
    #materia = "Matematicas"
    sepEstud = notasEstud.split(";") #esto separa los datos y se genera un lista
    #nombEstNotas = {} #declarar diccionario vacio
    nombEstNotas = dict()
    
    
    for i in sepEstud:
        #print("Variable i: ", i)
        
        sepNotas = i.split(",")
        #print(sepNotas) # resultado lista notas
        
        nombEstNotas[sepNotas[0]]=0
        
        for k in range(1, len(sepNotas)):
            nombEstNotas[sepNotas[0]]+=eval(sepNotas[k])
            
        #nombEstNotas[sepNotas[0]] /= k
        
    return (materia, nombEstNotas)
    