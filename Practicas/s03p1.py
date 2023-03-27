# colecciones : listas
lista1 = ["Python", "CSharp", "Java", "Javascript"]
# base 0
print(lista1[1] + " " + lista1[-1])  # CSharp Javascript
print(str(type(lista1)))  # lis
print(str(len(lista1)))  # 4
# con lista1[:] lista completa
# con lista1[0:3] elementos 0,1,2 (el 3 no)
# con lista1[2:] elementos desde el 2 hasta el final
# a diferencia de otros lenguajes podemos combinar distintos tipos
lista3 = ["Python", 100, 25, " ", True, 17.5]
for elemento in lista3:
    print(type(elemento))  # str int int str bool float
# con Range podemos generar un conjunto de valores numericos
lista4 = list(range(1, 10, 2))  # en este caso del 1 al 10 y con step 2
print(lista4[1])  # 3
print(dir(lista1))  # con dir sacamos los métodos que podemos aplicar a un objeto
# a diferencia de otros lenguajes, podemos añadir dinamicamente
lista1.append("C++")  # añade un elemento al final
lista1.extend(["VBA", "R"])  # añade un conjunto al final
# podemos sumar listas con el operador + : listanueva = lista 1 + lista2
# con el multiplicador lo que hace es repetir los elementos: listanueva = lista1 * 3
lista1.insert(3, "HTML")  # inserta un elemento en la posicion indicada
print(lista1)  # [ Python , CSharp , Java , HTML , Javascript , C++ , VBA , R ]
lista1.pop()  # elimina el ultimo elemento
lista1.pop(2)  # elimina el elemento de la posicion indicada
lista1.remove("CSharp")  # elimina por valor (si hubiera varios elimina el primero)
print(lista1)  # [ Python , HTML , Javascript , C++ , VBA ]
print(lista1.count("CSharp"))  # cuenta las veces que encuentra un elemento
# podemos utilizar in para comprobar si hay un valor
print("Csharp" in lista1)  # False
print("C++" in lista1)  # True
# con lista1.index("Java") devuelve 2
lista1.sort()  # ordena los elementos
print(lista1)  # [ C++ , HTML , Javascript , Python , VBA ]
lista4.sort(reverse=True)  # ordena de forma inversa
print(lista4)  # [9, 7, 5, 3, 1]
lista1.clear()  # elimina todos los elementos
print(lista1)  # [ ]
del lista1  # elimina el objeto
# print(lista1) esta da un error porque el objeto ya no existe
# con varias dimensiones
lista5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(lista5[2][0])  # 7
print(str(len(lista5)))  # para devolver el numero de filas
print(str(len(lista5[0])))  # para devolver el numero de columnas
# de esta forma haria las combinaciones
for x in lista3:
    for y in lista4:
        print(x, y)
    # Python 9
    # Python 7
    # Python 5
    # Python 3
    # Python 1
    # 100 9
    # 100 7
    # ...
