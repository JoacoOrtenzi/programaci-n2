from ast import While
from operator import truediv
import random        
IMAGENES_AHORCADO = ['''        
  +---+        
  |   |        
      |        
      |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
      |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
  |   |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|   |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|\  |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|\  |        
 /    |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|\  |        
 / \  |        
      |        
  =========''']        
#aca van variables
letrasProbadas=[]
PALABRAS = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()
#aca van funciones
debeJugar=True
letrasProbadas=[]
letrasValidas=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
def generarPalabra (PALABRAS):
    palabraSecreta=PALABRAS[random.randint(1,len(PALABRAS)-1)]
    return palabraSecreta
def jugarDeNuevo ():
    jDNp=input("¿Desea jugar de nuevo? si/no").upper()
    if jDNp=="SI":
        jDN=True
    else:
        jDN=False
    return jDN
def obtenerIntento (palabraSecreta , letrasProbadas)
    intento=1
    while intento==1:
        intento=("Ingrese una letra a probar")
        if len(intento)!= 1:
            print("debe ingresar un solo caracter")
        else:
            
    

#Programa
while(debeJugar==True):
    palabraSecreta=generarPalabra()
    print(palabraSecreta)