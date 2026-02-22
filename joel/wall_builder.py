def wall_builder():
    width = int(input("Ingrese el ancho de la muralla: "))
    height = int(input("Ingrese el alto de la muralla: "))

    print("\nConstruyendo muralla...\n")

    for row in range(1, height + 1):
        for column in range(1, width + 1):

            if row == 1 or row == height or column == 1 or column == width:
                print("#", end="")
            else:
                print(" ", end="")

        print()


wall_builder()
