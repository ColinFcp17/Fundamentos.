mas_de_15 = 0
menos_o_igual_15 = 0

# Ingresar cantidad de libros
cantidad = int(input("Ingrese la cantidad de libros: "))

# Registrar libros
for i in range(cantidad):
    titulo = input(f"Libro {i + 1} - Título: ")
    dias = int(input("Cantidad de días de préstamo: "))

    if dias > 15:
        mas_de_15 += 1
    else:
        menos_o_igual_15 += 1

# Mostrar resultados
print(f"\nLibros con préstamo mayor a 15 días: {mas_de_15}")
print(f"\nLibros con préstamo de 15 días o menos: {menos_o_igual_15}")