# Lista vacía para almacenar productos

lista_compras = []


print("Bienvenido a tu lista de compras en Python")


# Agregar productos

producto1 = input("Ingresa el primer producto: ")

producto2 = input("Ingresa el segundo producto: ")


lista_compras.append(producto1)

lista_compras.append(producto2)


# Mostrar la lista

print("Lista actual de compras:", lista_compras)


# Modificar un producto

producto_mod = input("¿Deseas cambiar el segundo producto? Escribe el nuevo: ")

lista_compras[1] = producto_mod

print("Lista actualizada:", lista_compras)


# Eliminar un producto

producto_eliminar = input(" ¿Qué producto quieres eliminar?: ")

if producto_eliminar in lista_compras:

  lista_compras.remove(producto_eliminar)

  print("Producto eliminado.")

else:

  print(" Ese producto no está en la lista.")


# Mostrar el total

print(" Total de productos en tu lista:", len(lista_compras))

print(" Lista final:", lista_compras)