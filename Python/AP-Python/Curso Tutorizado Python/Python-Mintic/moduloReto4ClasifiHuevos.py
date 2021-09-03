def clasificacion_huevos(listaTamHuevo):
    #Definir las variables para clasificar los recipientes
    
    tipoHuevo_A ={
        "tipo_huevo":"A",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    tipoHuevo_AA ={
        "tipo_huevo":"AA",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    tipoHuevo_AAA ={
        "tipo_huevo":"AAA",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    tipoHuevo_BC ={
        "tipo_huevo":"BC",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    
    for tamHuevo in listaTamHuevo:
        if tamHuevo >= 53 and tamHuevo <= 60:
            tipoHuevo_A["numero_huevos"]+=1
        
        elif tamHuevo > 60 and tamHuevo <= 67:
            tipoHuevo_AA["numero_huevos"]+=1
        
        elif tamHuevo > 67:
            tipoHuevo_AAA["numero_huevos"]+=1
            
        elif tamHuevo > 0 and tamHuevo <= 53:
            tipoHuevo_BC["numero_huevos"]+=1
            
        
    
    # Fuera del For
    #Hallar la cantidad de cajas para cada tipo de recipiente
    
    tipoHuevo_A["numero_bandejas"] = tipoHuevo_A["numero_huevos"] // 30
    tipoHuevo_AA["numero_bandejas"] = tipoHuevo_AA["numero_huevos"] // 24
    tipoHuevo_AAA["numero_bandejas"] = tipoHuevo_AAA["numero_huevos"] // 12
    tipoHuevo_BC["numero_bandejas"] = tipoHuevo_BC["numero_huevos"] // 30
    
    
    clasifHuevo = [tipoHuevo_A, tipoHuevo_AA, tipoHuevo_AAA, tipoHuevo_BC]
    
    return clasifHuevo