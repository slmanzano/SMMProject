print("Hola Mundo") # comentarios
# comentarios multilinea
""" comentario
multilinea"""

# utilización de caracteres especiales
print("saludos\ndesde Python")
print("saludos\tdesde C#")

a = "saludos"
b = "desde Python"
print(a + " " + b)

# texto multilinea
cadenalarga = """texto extenso
escrito en
varias lineas"""
print(cadenalarga)
# tambien se podria hacer con comillas simples '''

x = 100
y = 50
print(x + y)
z = x*(y+20)
print(z) # 7000

# declarar y asignar varias variables en una linea
r,s,t = "Madrid","Barcelona", 100
print(r + s) # MadridBarcelona

# asignando el mismo valor
m = n = p = q = 10
print(m + n + p + q) # 40

# conversion explicita
n1 = str(10)
print(n1 + "50") # 1050

# con coma (,) no es necesario convertir para concatenar los que no sean texto
print(10 , "50") # 1050

# se puede concatenar tambien asi sin necesidad de conversiones
variable = 100
print(f"saludos desde {variable}")

n2 = int(27.5)
print(n2) # 27
n3 = float(27)
print(n3) # 27.0

# para sacar el tipo de una variable
print(type(z)) # int
print(type(10/7)) # float
print(type(str(100))) # str
a = True
b = False
print(a , type(a)) # True bool

# > , < , >= , <= , == , !=
print(100>99 , type(100>99)) # True bool

# and , or
print(a and 100>101) # False
print(a or 100>101) # True