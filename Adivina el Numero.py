import random

print("Bienvenido al juego de adivinar el numero")

while True:

    Menor = int(input("Ingrese un número menor: "))
    Mayor = int(input("Ingrese un número mayor: "))


    if Menor >= Mayor:
        print("Error: el numero menor debe ser menor que el mayor.")
    else:
        break
print(f"los numeros ingresados {Menor} y {Mayor}")
numero = random.randint(Menor, Mayor)
numero = round(numero / 4) * 4


for Intento in range(1, 4):
        adivina = int(input(f"Intento {Intento}: Adivina el numero: "))


if adivina == numero:
        print("¡Enhorabuena Adivinaste el número!")
   
elif Intento == 2:
        if adivina < numero:
            print("Pista: El número es MAYOR")
        else:
            print("Pista: El número es MENOR")
elif Intento == 3:
        print(f"Perdiste. El número era: {numero}")