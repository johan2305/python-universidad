print("🧮 Bienvenido a la calculadora")

# pedir los numero con validacion
while True:
    try:
        num1 = float(input("Escribe el primer número: "))
        num2 = float(input("Escribe el segundo número: "))
        break
    except:
        print("error: escribe numero validos. \n")

# mostrar el numero
print("\nElige una operación:")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

op = input("opcion: ")

# procesar la operacion
if op == "1":
    print("resultado:", num1 + num2)
elif op == "2":
    print("resultado:", num1 - num2)
elif op == "3":
    print("resultado:", num1 * num2)
elif op == "4":
    if num2 !=0:
        print("resultado:", num1 / num2)
    else:
        print("no se puede dividir entre cero.")
else:
    print("opcion invalida")


