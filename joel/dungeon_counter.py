def dungeon_counter():
    total_rooms = int(input("Ingrese la cantidad de salas del dungeon: "))

    for room_number in range(1, total_rooms + 1):

        if room_number % 3 == 0 and room_number % 5 == 0:
            print("Sala", room_number, ": Sala legendaria")

        elif room_number % 3 == 0:
            print("Sala", room_number, ": Sala con trampa")

        elif room_number % 5 == 0:
            print("Sala", room_number, ": Sala con tesoro")

        else:
            print("Sala", room_number, ": Sala normal")


dungeon_counter()
