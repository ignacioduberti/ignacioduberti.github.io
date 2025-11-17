Partida = 5


print ("-------------");
print ("|Bienvenido.|");
print ("------------- ");

for i in range (Partida):
    
    print ("")
    print ("-------------------------------")
    print(f"PARTIDA NÚMERO {i + 1}") 
    print ("selecciona la cantidad de vida");
    print ("-------------------------------")
    print ("")
    vida = int (input("_ ")) 

    if vida >= 5:
        print ("")
        print("El nivel de dificultad sera: Facil")
    elif vida >= 3 and vida <= 4:
        print ("")
        print ("El nivel de dificultad sera: Medio")
    elif vida <=2:
        print ("")
        print ("El nivel de dificultad sera: Dificl")
    else:
        print ("")
        print ("Nivel no valido")