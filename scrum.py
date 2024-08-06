import random
import emoji
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print(Fore.GREEN + "¡Bienvenido al juego de Adivina el Número!")
    print(Fore.GREEN + "Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            adivinanza = int(input(Fore.CYAN + "Adivina el número: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print(Fore.YELLOW + "Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print(Fore.YELLOW + "Demasiado alto. Intenta de nuevo.")
            else:
                # Usa emoji para la felicitación
                print(Fore.CYAN + f"{emoji.emojize(':trophy:')} ¡¡Felicidades!! Adivinaste el número en {intentos} intentos.")
                break

        except ValueError:
            print(Fore.RED + "Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()
