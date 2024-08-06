import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 100.")

while True:
    try:
        adivinanza = int(input("Adivina el número: "))
        intentos += 1
        if adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Intente de nuevo.")
        else:
            print(f"¡¡Felicidades!! Adivinaste el numero en {intentos} intentos.")
            break
            except ValueError:
                print("Por favor, ingresa un numero valido.")
        if __name__=="__main__":
            adivina_el_numero()
    

