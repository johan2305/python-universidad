import random

print("🎮 Bienvenido al juego de adivinar el número")
print("Estoy pensando en un número del 1 al 10...")

numero_secreto = random.randint(1, 10)

intento = int(input("Adivina el numero: "))

if intento == numero_secreto:
    print("🎉 ¡Correcto! Ese era el número.")
elif intento > numero_secreto:
    print("📉 Muy alto. Intenta con un número más pequeño.")
else: 
    print("📈 Muy bajo. Intenta con un número más grande.")