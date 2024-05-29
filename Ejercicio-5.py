
def crearLista():
    tempDias = []
    for temp in range(2):
        temp = int (float(input("Cual fue la temperatura de los ultimos 6 dias?: ")))
        tempDias.append(temp)

    return tempDias

def hayPositivos(lista):

    diasFrios = 0 

    for t in lista:   
        if t >= -10 and t < 5:
            diasFrios = diasFrios + 1

    return diasFrios


listaNueva = crearLista()
print(listaNueva)

if hayPositivos(listaNueva):
    print(f"hubieron ")
else:
    print("No hay positivos")



