import random

print("🎮 Bienvenido al juego avanzado de adivinar el número")
print("Estoy pensando en un número del 1 al 10...")

numero_secreto = random.randint(1, 10)
adivinado = False  # una bandera que dice si acertaste o no

while not adivinado:
    intento = int(input("Adivina el número: "))

    if intento == numero_secreto:
        print("🎉 ¡Correcto! Ese era el número.")
        adivinado = True
    elif intento > numero_secreto:
        print("📉 Muy alto. Intenta con un número más pequeño.")
    else:
        print("📈 Muy bajo. Intenta con un número más grande.")
