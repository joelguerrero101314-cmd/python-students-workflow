import random


def guardian_number():
    secret_number = random.randint(1, 20)
    max_attempts = 5
    attempt_count = 0
    is_open = False

    print("El guardián protege un número secreto entre 1 y 20.")
    print("Tienes 5 intentos para abrir la puerta.")

    while attempt_count < max_attempts:
        user_guess = int(input("Ingrese un número: "))
        attempt_count += 1

        if user_guess == secret_number:
            print("¡Correcto! La puerta se ha abierto.")
            print("Intentos usados:", attempt_count)
            is_open = True
            break
        elif user_guess > secret_number:
            print("Demasiado alto.")
        else:
            print("Demasiado bajo.")

    if not is_open:
        print("La puerta permanece cerrada.")
        print("El número secreto era:", secret_number)


guardian_number()
