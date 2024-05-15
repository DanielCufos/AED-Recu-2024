numeros = []

for num in range(7):
    num = int(input("Decime un numero: "))
    numeros.append(num)

print(numeros)

NumPositivo = False

for n in numeros:   
    if n > 0:
        NumPositivo = True


if NumPositivo:
    print("hay positivos")

else:
    print("No hay positivos")
