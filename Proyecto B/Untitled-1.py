print ("-------------");
print ("|Bienvenido.|");
print ("------------- ");
print ("selecciona la cantidad de vida");
print ("")
vida = int (input("_ ")) 

if vida >= 5:
        print("El nivel de dificultad sera: Facil")
elif vida >= 3 and vida <= 4:
        print ("El nivel de dificultad sera: Medio")
elif vida <=2:
        print ("El nivel de dificultad sera: Dificl")
else:
        print ("Nivel no valido")