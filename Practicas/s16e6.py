from io import StringIO , BytesIO , open
from functools import reduce

textos = ["Mario","Alberto","Monica","Sara","Esther","Rafael","Ramon", "Jose Luis","Ramon","Maria","Juan","Alberto","Monica", "Javier","Javier","Luis","Mario","Lucia","Alberto"]

texto = reduce(lambda a,b : a + " " + b , textos)
texto2 = list(map(lambda a : "\n" + a , textos))

# StringIO nos permite trabajar en un objeto en memoria como si
# se tratara de un archivo
# objeto StringIO utilizado para escritura
escritura = StringIO()
escritura.write(texto)
escritura.write("\n")
escritura.writelines(texto2)

# si lo tratamos como si fuera para lectura
escritura.seek(0)
print(escritura.read())
escritura.seek(0)
print(escritura.readlines())
escritura.seek(0)

# si lo queremos volcar a un archivo
with open("archivo_texto.txt", "w") as f:
    f.writelines(escritura.readlines())

escritura.close() # libera la memoria del objeto

# analogamente tenemos BytesIO para binario
# escritura_binaria = BytesIO()
# escritura_binaria.write(contenido binario)