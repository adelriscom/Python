import requests
from bs4 import BeautifulSoup

miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text, "html.parser")

iconos=docFinal.select(".emoji")
titulos=docFinal.select(".card-title span")
contenidos=docFinal.select(".card-text")

#print(iconos[0])
#print(iconos[0].text)
#print(titulos[1].text)
#print(contenidos[0].text)

#for cuerpoTexto in docFinal.select(".card-text"):
    
    #print(cuerpoTexto.text)
    #print(" ")
    

for imagen in docFinal.select(".card-block img"):
    
    print(imagen.attrs["src"])
    print(" ")






    


    