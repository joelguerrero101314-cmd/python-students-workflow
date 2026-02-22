def player_console():
    lives = 3

    while True:
        print("\n=== CONSOLA DEL JUGADOR ===")
        print("1. Ganar una vida")
        print("2. Perder una vida")
        print("3. Ver estado")
        print("4. Salir")

        option = int(input("Seleccione una opción: "))

        if option == 1:
            lives += 1
            print("Has ganado una vida.")

        elif option == 2:
            if lives > 0:
                lives -= 1
                print("Has perdido una vida.")
            else:
                print("No puedes tener vidas negativas.")

        elif option == 3:
            print("Vidas actuales:", lives)

        elif option == 4:
            print("Saliendo del juego...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


player_console()
