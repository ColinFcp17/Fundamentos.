total = 0

pino = int(input("Empanadas de pino ($2000) cantidad: "))
queso = int(input("Empanadas de queso ($1500) cantidad: "))
chori = int(input("Choripanes ($2500) cantidad: "))
terremoto = int(input("Terremotos ($1000) cantidad: "))

total += pino * 2000
total += queso * 1500
total += chori * 2500
total += terremoto * 1000

if total > 20000:
    desc = 0.4
    print("Descuento 40% aplicado y entradas GRATIS")
elif total > 10000:
    desc = 0.25
    print("Descuento 25% aplicado y entradas GRATIS")
else:
    desc = 0
    print("Sin descuento")

final = int(total * (1 - desc))
print(f"Total a pagar: ${final}")