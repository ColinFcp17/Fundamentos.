import time

print('Hola, hoy día calculare el área de varios triángulos')

Altura_triangulo = float(input('Medida Altura: '))
print(Altura_triangulo,'cm')

Base_triangulo = float(input('Medida Base: '))
print(Base_triangulo,'cm')

print('1.- Equilatero')
print('2.- Isósceles')
print('3.- Escaleno')
print('4.- Acutángulo')
print('5.- Rectángulo')
print('6.- Obtusángulo')

while True:
    try:
        Opcion = int(input('Elegi una opción (Numero): '))
        if Opcion > 0 and Opcion <= 6:
            break
        else:
            print('Error, el número fuera del rango')
    except ValueError:
        print('ERROR... El número debe ser un entero, intenta otra vez')

match Opcion:
    case 1:
        print('Eligió el triángulo Equilátero')
    case 2:
        print('Eligió el triángulo Isósceles')
    case 3:
        print('Eligió el triángulo Escaleno')
    case 4:
        print('Eligio el triángulo Acutángulo')
    case 5:
        print('Eligio el triángulo Rectángulo')
    case 6:
        print('Elige el triángulo Obtusángulo')

print('Ahora realizare el cálculo')
time.sleep(5)
print(f'({Altura_triangulo} x {Base_triangulo}) / 2 =')
time.sleep(2)

Area = (Base_triangulo * Altura_triangulo) / 2
print(Area, 'cm²')
time.sleep(2)

print('El área del triángulo que usted eligio es:', Area, 'cm²')
