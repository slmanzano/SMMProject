temperatura = 36.5

print("Apartado B\nVoy a crear la lista y mostrarla")
decim = 0.5
# como hay un salto de 0.5, la diferencia será multiplicada x2+1 para que coja el 42
def funcion1 (a, b):
    listaAux=[]
    diferencia = b - a
    for x in range(diferencia*2+1):
        listaAux.append(a)
        a += decim
    return listaAux

lista = funcion1(35, 42)
print("Mi lista:", lista)
#no consigo que el 35 lo guarde como float pero eso sería seguir dándole más vueltas hasta conseguirlo con un if


print("\n\nApartado C")

def funcion2 (listaaux):
    for x in lista:
        return lista

print("Llamo a la función que muestra mi lista usando un for:\n",funcion2(lista))


print("\n\nApartado D")

def funcion3(listaaux):
    i = 0
    while i < len(listaaux):
        if listaaux[i] == temperatura:
            print(listaaux[i], "*")
        else:
            print(listaaux[i])
        i += 1
    return 0

print("Llamo a la función que muestra el asterisco:")
funcion3(lista)


print("\n\nVoy a intentar el apartado E:")
def funcion4(listaaux, temp):
    if temp < 35 or temp > 42:
        print("El valor", temp, "no está en el rango\n")
    else:
        i = 0
        contador = 0
        while i < len(listaaux):
            if listaaux[i] == temp:
                print("El valor de temperatura buscado", temp, "existe en la lista")
                print("Veces que ha pasado por el else:", contador,"\n")
                break
            else:
                i += 1
                contador += 1

print("Llamo a la función que encuentra el valor de la temperatura:\n")
#pruebo con diferentes valores
funcion4(lista, temperatura) #debe salir 3 (sin haber contado el 35)
funcion4(lista, 40.0) #debe salir 10
funcion4(lista, 42) #debe salir 14, la longitud de la lista al ser el último elemento
funcion4(lista, 20) #debe decir que no existe
