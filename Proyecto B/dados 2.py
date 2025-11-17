import random

Puntuacion1 = 0
Puntuacion2 = 0
intentosJ1 = 0
intentosJ2 = 0

print ("")
print ("----------------------------------")
print ("¿cuantos intentos desesa realizar?")
print ("----------------------------------")
print ("")

intentosJ1 = int (input("_ "))
intentosJ2 = intentosJ2 + intentosJ1
print ("")

while True:

    if intentosJ1 > 0:

        print ("")
        print("----------")
        print("JUGADOR 1")
        print("----------")
        print ("")

        dad1 = random.randint (1, 6)
        dad2 = random.randint (1, 6)
        tirada = dad1 + dad2;
        Puntuacion1 = Puntuacion1 + tirada;

        print ("sacaste ",dad1," + ",dad2," = ",tirada )
        
        intentosJ1 = intentosJ1 - 1

    if intentosJ2 > 0:

        print ("")
        print("----------")
        print("JUGADOR 2")
        print("----------")
        print ("")
        dad1 = random.randint (1, 6)
        dad2 = random.randint (1, 6)
        tirada = dad1 + dad2
        Puntuacion2 = Puntuacion2 + tirada

        print ("sacaste ",dad1," + ",dad2," = ",tirada )
        
        intentosJ2 = intentosJ2 - 1

        if intentosJ1 == 0 and intentosJ2 == 0:
            print ("")
            print ("------------------")
            print ("|PUNTUACION FINAL|")
            print ("------------------")
            print ("")
            print (" J1  /  J2 ")
            print ("|",Puntuacion1," / ",Puntuacion2,"|")
            print ("")
            print ("EL GANADOR ES:")
            print ("")

            if Puntuacion1 > Puntuacion2:

                print("----------")
                print("JUGADOR 1")
                print("----------")
                break

            else:

                print("----------")
                print("JUGADOR 2")
                print("----------")
                break
    else:
        print ("numero invalido")
        break
    