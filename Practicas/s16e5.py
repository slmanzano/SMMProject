from io import open

# con la siguiente sentencia se crea el archivo y se abre para escritura
escritura = open("archivo_texto.txt", "w")
# segundo parametro tipo de apertura (en este caso write)
print(type(escritura)) # TextIOWrapper
print(escritura.mode) # w
# print(escritura.read()) # si intentamos hacer operaciones de lectura daria error

# con write volcamos flujo de texto
texto = "este texto se va a guardar en el archivo creado"
escritura.write(texto)
escritura.write("\n")
escritura.write("mas texto")
# con writelines() escribe un conjunto de textos
escritura.writelines(["\n","otro mas".upper(), "y otro".upper()])
escritura.close()
# escritura.write("www") esto daria error
# si una vez que hemos cerrado con close () queremos seguir escribiendo
# lo abrimos en modo añadir (segundo parametro "a")
# si volvemos a utilizar "w" el archivo se reescribiria desde cero
escritura2 = open("archivo_texto.txt", "a")
escritura2.write("5439684598764586794")
escritura2.close()

# para abrir el archivo para su lectura (segundo parametro "r")
lectura = open("archivo_texto.txt", "r", encoding="utf-8")
print(type(lectura)) # TextIOWrapper

# readlines() obtiene una lista con las diferentes lineas del texto
# si al escribir no hubiera metido saltos de linea la lista
# tendria 1 solo elemento (1 sola linea)
for linea in lectura.readlines():
    print(linea)
print("-----------------------------------")

# con seek() puedo mover el puntero de lectura a la posicion deseada
# en este caso voy a desplazar el puntero al principio
# para poder vover a leer su contenido
lectura.seek(0)
print(lectura.read()) # con read() lee el contenido entero
print("-----------------------------------")
lectura.seek(0)
print(lectura.read(7)) # lee solo hasta la posicion 7 (no incluida)
# si a continuacion hacemos read() leeria desde ahi hasta el final
print("-----------------------------------")
# con readline() va leyendo linea por linea
lectura.seek(0)
print(lectura.readline()) # primera linea
print(lectura.readline()) # primera linea
print(lectura.readline()) # primera linea
print(len(lectura.readline()))
# como solo habia 3 lineas por leer el 4o readline() devuelve vacio
lectura.close()
print("-----------------------------------")

# con el segundo parametro "r+" permite tanto lectura como escritura
mixto = open("archivo_texto.txt", "r+")
print(mixto.mode) # r+
lista_lineas = mixto.readlines()
print(lista_lineas)
mixto.write("\n00000000000") # se escribe al final de las otras lineas
mixto.close()
print("-----------------------------------")

# otra sintaxis
with open("archivo_texto.txt", "r") as l:
    print(l.readlines())

# con los modos "wb" y "rb" realizamos escritura y lectura de archivos binarios