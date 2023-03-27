nombre = "Sara Lucía"
apellidos = "Manzano Membrilla"
dia = str(3)
mes = str(7)
year = str(1995)
fechanacimiento = dia + "/" + mes + "/" + year
altura = 174
temperatura = float(36.1)

tupla = (nombre, apellidos, fechanacimiento, altura, temperatura)
print(tupla)

lista = list(tupla)
lista[4] = temperatura + 0.5
print(lista[4])

tupla= tuple(lista)
print(tupla)