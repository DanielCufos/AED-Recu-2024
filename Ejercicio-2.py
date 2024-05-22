
def crearLista():
    numero = []
    for num in range(7):
        num = int(input("Decime un numero: "))
        numero.append(num)

    return numero


listaNueva = crearLista()

print(listaNueva)

def hayPositivos(lista):

    NumPositivo = False

    for n in lista:   
        if n > 0:
            NumPositivo = True

    if NumPositivo:
        return True

    else:
        return False

if hayPositivos(listaNueva) == True:
    
    print("Hay positivos")

else:
    print("No hay positivos")



