contraseña = input("ingrese la contraseña: ")

longitud = len(contraseña)

if longitud < 4:
    print("contraseña muy debil ❌")
elif longitud < 7:
    print("contraseña debil ⚠️")
elif longitud < 11:
    print("Contraseña buena 👍")
else:
    print("Contraseña fuerte 🔥")