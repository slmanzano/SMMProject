numeros = [3,23,16,34,87,26,31,7,23,6,23,58,29,71,4,4,32,37,60]
textos = ["Mario","Alberto","Monica","Sara","Esther","Rafael","Ramon","Jose Luis","Ramon",
"Maria","Juan","Alberto","Monica","Javier","Javier","Luis","Mario","Lucia","Alberto"]
# con 'List_Comprehension' nos permiten una sintaxis abreviada para obtener
# a partir de un conjunto un subconjunto de elementos que cumplan condiciones
# todos los numeros
print(list(n for n in numeros))
# numeros mayores de 10
print(list(n for n in numeros if n > 20))
# textos con 5 caracteres
print(list(t for t in textos if len(t)==5))
print("")
# podemos transformar el resultado
print(list(n + 100 for n in numeros if n > 60))
print(list(str(n).replace("1","X") for n in numeros if n > 30))
print("")
# combinando 2 listas
print(list(textos[n] for n in numeros if n < 19))
# si >= 19 se sale de la lista textos
print(list((n,t) for n in numeros for t in textos if n >= 71 and t == "Alberto"))
# hace combinaciones
print("")
# podemos construirlas utilizando corchetes
# entonces no es necesario la conversión a list()
numeros_pares = [i for i in range(11) if i % 2 == 0]
print(list)
paises_letra = [i for i in ["Angola","Portugal","Mejico","India","Luxemburgo","Andorra"] if "a" not in i or "A" not in i]
print(paises_letra)
numeros_multiplicacion = [i*10 for i in range(1, 6) if i != 4]
print(numeros_multiplicacion)
print(["Mexico" if i == "Mejico" else i for i in ["Angola","Portugal","Mejico","India","Luxemburgo","Andorra"] ])