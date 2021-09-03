import random
#Clasificacion de recipientes utilizando listas de datos, diccionarios y funciones

#Declaracion de la funcion

def clasificacion_recipientes(listaVolumenRecipiente):
    #Definir las variables para clasificar los recipientes
    
    tipoRecipCopa ={
        "tipoRecip":"Copa",
        "cantRecip":0,
        "cantCajas":0
    }
    tipoRecipVaso ={
        "tipoRecip":"Vaso",
        "cantRecip":0,
        "cantCajas":0
    }
    tipoRecipFrasco ={
        "tipoRecip":"Frasco",
        "cantRecip":0,
        "cantCajas":0
    }
    tipoRecipBotPeq ={
        "tipoRecip":"BotPeq",
        "cantRecip":0,
        "cantCajas":0
    }
    tipoRecipBotMed ={
        "tipoRecip":"BotMed",
        "cantRecip":0,
        "cantCajas":0
    }
    tipoRecipBotGrand ={
        "tipoRecip":"BotGrand",
        "cantRecip":0,
        "cantCajas":0
    }
    tipoRecipDescart ={
        "tipoRecip":"Descartado",
        "cantRecip":0,
        "cantCajas":0
    }
    
    for volRecip in listaVolumenRecipiente:
        if volRecip >= 40 and volRecip <= 60:
            tipoRecipCopa["cantRecip"]+=1
        
        elif volRecip >= 80 and volRecip <=120:
            tipoRecipVaso["cantRecip"]+=1
        
        elif volRecip >= 140 and volRecip <= 200:
            tipoRecipFrasco["cantRecip"]+=1
            
        elif volRecip >= 210 and volRecip <= 280: #volRecip ==250:
            tipoRecipBotPeq["cantRecip"]+=1
            
        elif volRecip >= 300 and volRecip <= 500:
            tipoRecipBotMed["cantRecip"]+=1
        
        elif volRecip >= 600 and volRecip <= 1000:
            tipoRecipBotGrand["cantRecip"]+=1
            
        else:
            tipoRecipDescart["cantRecip"]+=1
    
    # Fuera del For
    #Hallar la cantidad de cajas para cada tipo de recipiente
    
    tipoRecipCopa["cantCajas"] = tipoRecipCopa["cantRecip"]//10
    tipoRecipVaso["cantCajas"] = tipoRecipVaso["cantRecip"]//6
    tipoRecipFrasco["cantCajas"] = tipoRecipFrasco["cantRecip"]//40
    tipoRecipBotPeq["cantCajas"] = tipoRecipBotPeq["cantRecip"]//30
    tipoRecipBotMed["cantCajas"] = tipoRecipBotMed["cantRecip"]//20
    tipoRecipBotGrand["cantCajas"] = tipoRecipBotGrand["cantRecip"]//10
    tipoRecipDescart["cantCajas"] = tipoRecipDescart["cantRecip"]//100
    
    clasifRecip = [tipoRecipCopa, tipoRecipVaso, tipoRecipFrasco, tipoRecipBotPeq, tipoRecipBotMed, tipoRecipBotGrand, tipoRecipDescart]
    
    return clasifRecip

