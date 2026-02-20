# Practica 1: El Guardian del Numero

def main():
    secret_number = 12
    continues = 0
    max_continues = 5

    print("\n\t==============================")
    print("\t     EL GUARDIAN DEL NUMERO")
    print("\t==============================\n")

    while continues < max_continues:
        number = int(input("Ingrese un numero entre 1 y 20: "))
        continues = continues + 1

        if number == secret_number:
            print("\n\tLa puerta se ha abierto")
            print("\tIntentos realizados: " + str(continues))
            continues = max_continues
        elif number < secret_number:
            print("\tDemasiado bajo")
        else:
            print("\tDemasiado alto")

    if number != secret_number:
        print("\n\tLa puerta permanece cerrada")

main()