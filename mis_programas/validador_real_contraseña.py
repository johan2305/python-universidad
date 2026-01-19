contraseña = input("Ingresa una contraseña: ")

tiene_mayus = any(letra.isupper() for letra in contraseña)
tiene_minus = any(letra.islower() for letra in contraseña)
tiene_num = any(letra.isdigit() for letra in contraseña)

if len(contraseña) >= 8 and tiene_mayus and tiene_minus and tiene_num:
    print("Contraseña valida 🔥")
else:
    print("Contraseña inválida ❌")