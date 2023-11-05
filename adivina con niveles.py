import random
n=0
intentosmax=0
intentos=0
secreto= random.randint (0,0)
df1=0
df2=0
df=0
df=(int(input("En que nivel desea jugar? " "1=facil " "2=dificil ")))
if df==1:
    intentosmax=6
    secreto= random.randint (1,20)
else:
    intentosmax=7
    secreto= random.randint (1,200)
while(intentosmax<intentos):
    n=(int(input("¿cual crees que es el numero?")))
    intento=int(input())
    if(n==secreto):
        print("adivinaste el numero ",secreto)
        break
    if(n>secreto):
            print("el numero es mayor al numeros secreto")
    else:
        print("el numero es menor al numero secreto")