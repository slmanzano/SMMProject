#def funcion1():
#print("saludos desde una funcion")
from typing import List, Union, Any

funcion1 = lambda texto : str(texto).lower()
print("resultado de funcion1", funcion1("SAluDOs Desde una FUNCION"))


#def funcion2(a,b):
#print(a + " desde " + b)
#funcion2("saludos","Python")
funcion2 = lambda x , y : x + " desde " + y
print("resultado de funcion2", funcion2("saludos","Python"))


#def funcion4(x,y,z):
#return x+y+z
funcion3 = lambda x , y, z : x + y + z
print("resultado de funcion3", funcion3(2,3,4))


#def funcion5(r,s):
#return r % s
funcion4 = lambda x , y : x % y
print("resultado de funcion4", funcion4(2,3))


#por practicar hago la práctica3
lista = [35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0]
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

#a) utiliza reduce para calcular la suma de todos los valores de la lista.
print(reduce(lambda x, y: x + y, lista))
sumatotal = reduce(lambda x, y: x + y, lista)
#la media sería esa sumatotal entre el número de elementos (15)
media = sumatotal/15
print(media)

#b) utiliza reduce para calcular la media de todos los valores de la lista.
print(reduce(lambda x, y: x + y, lista) / float(len(lista)))