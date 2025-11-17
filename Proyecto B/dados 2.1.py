import random

def tiradas():
    tiradas=0
    print ("ingrese las tiradas que van a realizar")
    print ("")
    intentos = int (input("_"))
    for i in range(intentos):
        dad1 = random.randint (1, 6)
        dad2 = random.randint (1, 6)
        tirada = dad1 + dad2;
        Puntuacion1 = Puntuacion1 + tirada;
    return tiradas 
