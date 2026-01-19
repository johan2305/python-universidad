amigos = ["juan", "pedro", "maria"]

print("lista original:", amigos)

amigos.append("laura")
print("despues de agregar:", amigos)

amigos[1] = "carlos"
print("despues de cambiar un elemento:", amigos)

del amigos[0]
print("despues de eliminar:", amigos)

print("numero de amigos:", len(amigos))