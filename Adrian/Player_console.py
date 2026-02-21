#File 2 player console

def main():
    lifes = 3
    option = 0

    while option != 4:

        print("\n\t==============================")
        print("\t      CONSOLA DEL JUGADOR")
        print("\t==============================\n")

        print("\t1. Ganar una vida")
        print("\t2. Perder una vida")
        print("\t3. Ver estado")
        print("\t4. Salir\n")

        option = int(input("Seleccione una opcion: "))

        if option == 1:
            lifes = lifes + 1
            print("\tHas ganado una vida")
        elif option == 2:
            if lifes > 0:
                lifes = lifes - 1
                print("\tHas perdido una vida")
            else:
                print("\tNo puedes tener vidas negativas")
        elif option == 3:
            print("\tVidas actuales: " + str(lifes))
        elif option == 4:
            print("\tSaliendo del juego...")
        else:
            print("\tOpcion no valida")

main()