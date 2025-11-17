import random

Puntuacion = 0;
intentos = 0;
print ("¿cuantos intentos desesa realizar?");
intentos = int (input("_ "));

while True:

    

    if intentos > 0:
        dad1 = random.randint (1, 6)
        dad2 = random.randint (1, 6)
        tirada = dad1 + dad2;
        Puntuacion = Puntuacion + tirada;

        print ("sacaste ",dad1," + ",dad2," = ",tirada )
        
        intentos = intentos - 1

        if intentos == 0:
                print ("puntuacion final = ", Puntuacion);
                break;
    
    else:
        print ("numero invalido");
    
