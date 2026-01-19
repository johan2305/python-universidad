clave_correcta = "30022305"

clave = input("escribe la contraseña: ")

while clave != clave_correcta:
    print("contraseña incorrecta,intenta de nuevo.")
    clave = input ("escribe la contraseña: ")

print("¡Acceso permitido!")