print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 100.")

while True:
    try:
        adivinanza = int(input("Adivina el número: "))
        intentos += 1
