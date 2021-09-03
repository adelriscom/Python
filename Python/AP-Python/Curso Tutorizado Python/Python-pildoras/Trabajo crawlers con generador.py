import requests, time, csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class PostCrawled():
    
    def __init__(self, titulo, emoticono, contenido, imagen):
        
        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido
        self.imagen=imagen        
        
        
class PostExtractor():
    
    def extraeInfo(self):
        
        urlBase="http://python.beispiel.programmierenlernen.io/index.php"
        
        #post=[] #Ya no se necesita una lista porque el generador devuelve uno a uno los elementos
        
        while urlBase !="":
            
            miDoc=requests.get(urlBase)
            docFinal=BeautifulSoup(miDoc.text, "html.parser")
            
            #detiene la ejecucion del bucle 2 seguindos
            time.sleep(2)
            
            #En este for each en la variable card almacenamos los diferentes elemento del objeto card, es decir titulo, emoticono, contenido e imagen
            for card in docFinal.select(".card"):
                
                titulo=card.select(".card-title span")[1].text
                emoticono=card.select_one(".emoji").text
                contenido=card.select_one(".card-text").text
                #imagen=card.select_one("img").attrs["src"]#ruta relativa a la imagen
                imagen=urljoin(urlBase, card.select_one("img").attrs["src"])#ruta absoluta a la imagen
                
                #crawled=PostCrawled(titulo, emoticono, contenido, imagen)#Se crea un objeto crawled de tipo PostCrawled
                #post.append(crawled)# Se agrega a la lista post el objeto crawled
                
                #DEFINICION DEL GENERADOR
                yield PostCrawled(titulo, emoticono, contenido, imagen) #GENERADOR
                
            #web2=docFinal.select_one(".navigation .btn").attrs["href"]#ruta relativa a la pagina principla
            
            #rutas_Absolutas=urljoin(urlBase, docFinal.select_one(".navigation .btn").attrs["href"])# ruta absoluta a la pagina principal
            
            boton_siguiente=docFinal.select_one(".navigation .btn")#Verifica que el boton existe
            
            #Este if valida la existencia del boton
            if boton_siguiente:
                
                rutas_Absolutas=urljoin(urlBase, boton_siguiente.attrs["href"])#construye la ruta absoluta
                urlBase=rutas_Absolutas   #Se reasigna el valor de la variable urlBase             
                print(rutas_Absolutas)
                
            else:
                urlBase=""#establese una cadena vacia a urlBase lo cual hace que salga del while en la siguente evaluacion
            
            
        #Devuelve la lista post 
        #return post 
    
unpost=PostExtractor()# CREACION DE OBJETO unpost TIPO postExtractor()

# "extraeInfo" ya no es un metodo, ahora es un generador. Trae la informacion de uno en uno
listaPost=unpost.extraeInfo()

#Este contador permite controlar el numero de posts retornados
contador=0 


#El for each definido tiene como finalidad recorrer la lista listaPost e ir almacenando los elementos en la variable elPost
for elPost in listaPost:
    
    if contador==12:
        break
    contador+=1
    
    print(elPost.titulo)
    print(elPost.emoticono)
    print(elPost.contenido)
    print(elPost.imagen)
    print()

print("AQUI EMPIEZA A ESCRIBIR LA LISTA listaPost")
#print(listaPost)

#Creacion de un archivo csv
with open('posts.csv', 'w', newline='') as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #for mipost in unpost.extraeInfo():
        #postwriter.writerow([mipost.emoticono, mipost.titulo, mipost.contenido, mipost.imagen])
        
    for mipost in listaPost:
        postwriter.writerow([mipost.emoticono, mipost.titulo, mipost.contenido, mipost.imagen])