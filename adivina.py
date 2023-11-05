import random
n=0
intentosmax=6
intentos=0
secreto= random.randint (1,20)
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
        
