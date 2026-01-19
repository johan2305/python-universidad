import json
import os

# ---------------------------------------
# Cargar datos desde archivo (si existe)
# ---------------------------------------
def cargar_datos():
    if os.path.exists("amigos.json"):
        with open("amigos.json", "r") as archivo:
            return json.load(archivo)
    return []


# ---------------------------------------
# Guardar datos en archivo
# ---------------------------------------
def guardar_datos(amigos):
    with open("amigos.json", "w") as archivo:
        json.dump(amigos, archivo, indent=4)


# ---------------------------------------
# Mostrar menú
# ---------------------------------------
def mostrar_menu():
    print("\n📘 GESTOR DE AMIGOS")
    print("1. Agregar amigo")
    print("2. Mostrar amigos")
    print("3. Buscar amigo")
    print("4. Editar amigo")
    print("5. Eliminar amigo")
    print("6. Eliminar varios amigos")
    print("7. Salir")


# ---------------------------------------
# Agregar amigo (evita duplicados)
# ---------------------------------------
def agregar_amigo(amigos):
    nombre = input("Nombre del amigo: ").strip()
    edad = input("Edad: ").strip()

    # Evitar nombres duplicados
    for amigo in amigos:
        if amigo["nombre"].lower() == nombre.lower():
            print("⚠️ Ese amigo ya existe, no se puede duplicar.")
            return

    amigos.append({"nombre": nombre, "edad": edad})
    guardar_datos(amigos)
    print("✅ Amigo agregado.")


# ---------------------------------------
# Mostrar amigos
# ---------------------------------------
def mostrar_amigos(amigos):
    if not amigos:
        print("📭 No hay amigos registrados.")
        return

    print("\n📋 Lista de amigos:")
    for i, amigo in enumerate(amigos):
        print(f"{i}. {amigo['nombre']} - {amigo['edad']} años")


# ---------------------------------------
# Buscar amigo
# ---------------------------------------
def buscar_amigo(amigos):
    texto = input("Ingresa texto a buscar: ").lower()

    resultados = [a for a in amigos if texto in a["nombre"].lower()]

    if resultados:
        print("\n🔎 Resultados:")
        for amigo in resultados:
            print(f"- {amigo['nombre']} ({amigo['edad']} años)")
    else:
        print("❌ No se encontraron coincidencias.")


# ---------------------------------------
# Editar amigo
# ---------------------------------------
def editar_amigo(amigos):
    mostrar_amigos(amigos)

    try:
        indice = int(input("Número del amigo a editar: "))
        if indice < 0 or indice >= len(amigos):
            print("❌ Índice inválido.")
            return

        nuevo_nombre = input("Nuevo nombre (Enter para no cambiar): ").strip()
        nueva_edad = input("Nueva edad (Enter para no cambiar): ").strip()

        # Evitar duplicados al editar
        if nuevo_nombre:
            for a in amigos:
                if a["nombre"].lower() == nuevo_nombre.lower() and a != amigos[indice]:
                    print("⚠️ Ese nombre ya existe en otro amigo.")
                    return
            amigos[indice]["nombre"] = nuevo_nombre

        if nueva_edad:
            amigos[indice]["edad"] = nueva_edad

        guardar_datos(amigos)
        print("✅ Amigo editado.")
    except ValueError:
        print("❌ Debes escribir un número.")


# ---------------------------------------
# Eliminar un amigo
# ---------------------------------------
def eliminar_amigo(amigos):
    mostrar_amigos(amigos)

    try:
        indice = int(input("Número del amigo a eliminar: "))
        if indice < 0 or indice >= len(amigos):
            print("❌ Índice inválido.")
            return

        amigos.pop(indice)
        guardar_datos(amigos)
        print("🗑️ Amigo eliminado.")
    except ValueError:
        print("❌ Debes escribir un número.")


# ---------------------------------------
# Eliminar varios amigos
# ---------------------------------------
def eliminar_varios(amigos):
    mostrar_amigos(amigos)

    indices = input("Escribe índices separados por coma (ej: 0,2,3): ")

    try:
        lista_indices = sorted({int(i) for i in indices.split(",")}, reverse=True)

        for i in lista_indices:
            if 0 <= i < len(amigos):
                amigos.pop(i)

        guardar_datos(amigos)
        print("🗑️ Varios amigos eliminados.")
    except ValueError:
        print("❌ Formato incorrecto.")


# ---------------------------------------
# Limpiar pantalla (opcional)
# ---------------------------------------
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


# ---------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------
def main():
    amigos = cargar_datos()

    while True:
        limpiar()
        mostrar_amigos(amigos)
        mostrar_menu()

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            agregar_amigo(amigos)
        elif opcion == "2":
            mostrar_amigos(amigos)
            input("Presiona Enter para seguir...")
        elif opcion == "3":
            buscar_amigo(amigos)
            input("Presiona Enter para seguir...")
        elif opcion == "4":
            editar_amigo(amigos)
            input("Presiona Enter para seguir...")
        elif opcion == "5":
            eliminar_amigo(amigos)
            input("Presiona Enter para seguir...")
        elif opcion == "6":
            eliminar_varios(amigos)
            input("Presiona Enter para seguir...")
        elif opcion == "7":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida.")
            input("Presiona Enter para seguir...")


if __name__ == "__main__":
    main()

