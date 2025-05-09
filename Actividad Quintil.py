Quintil = int(input("¿A que quintil perteneces?: "))

Condicion_Laboral = int(input("¿Cual es tu condicion Laboral: \n 1- para empleado. \n 2- para desempleado"))

Edad = int(input("Dime tu edad: "))

subsidio = 0

if Quintil == 1 and Condicion_Laboral == 2:
    subsidio = 15000

elif Quintil == 2 and Condicion_Laboral == 1:
    subsidio = 10000

elif Quintil == 3 and Condicion_Laboral == 2:
    subsidio = 8000

elif Quintil == 4 and Condicion_Laboral == 1:
    subsidio = 6000

elif Quintil == 5:
    subsidio = 1500

if Quintil == 1 or Quintil == 2:
    
    subsidio = subsidio + 2000

if Edad <= 65:
   
    subsidio = subsidio + 3000

print(f"Tu subsidio es: {subsidio}")