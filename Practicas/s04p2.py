temperatura = 36.5

lista = [35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0]

print("Este es el bucle for:")
for x in lista:
    print(x)

print("Ahora viene el bucle while:")
i = 0
while i < len(lista):
    if lista[i] != temperatura:
        print(lista[i])
    else:
        print(lista[i], "*")
    i += 1

print("Voy a intentar el apartado E:")
i = 0
contador = 0
while i < len(lista):
    if lista[i] == temperatura:
        print("El valor de temperatura buscado existe en la lista")
        print("Veces que ha pasado por el else:", contador)
        break
    else:
        i += 1
        contador += 1