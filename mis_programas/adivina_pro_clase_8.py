import  random

secreto = random.randint(1,10)
intentos = 0

while True:
    entrada = input("Adivina un número del 1 al 10: ")

    if not entrada.isdigit():
        print("❌ Eso no es un número. Intenta de nuevo.")

    numero = int(entrada)
    intentos += 1

    if numero == secreto:
        print("🎉 ¡Correcto! Lo lograste en", intentos, "intentos.")
        break
    elif numero < secreto:
        print("📉 Muy bajo.")
    else:
        print("📈 Muy alto.")


