import sys

texto = []

print("⬇⬇⬇ PEGA EL TEXTO LARGO AQUÍ ⬇⬇⬇")
print("(cuando termines, presiona Ctrl + Z y luego Enter)")

# AQUÍ el programa recibe el texto
for linea in sys.stdin:
    texto.append(linea)

texto_completo = "".join(texto)

print("Texto recibido:")
print(texto_completo)
