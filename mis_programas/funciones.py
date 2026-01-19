def saludar():
    print("hola, bienvenido al programa!")

def saludar_persona(nombre):
    print("hola", nombre)

def sumar(a, b):
    return a+b

# programa principal
saludar()

nombre_usuario=input("¿como te llamas? ")
saludar_persona(nombre_usuario)

num1 = int(input("escribe un numero: "))
num2 = int(input("escribe otro numero: "))

resultado = sumar(num1, num2)
print("la suma es:", resultado)