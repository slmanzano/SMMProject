nombre = "Sara Lucía"
apellidos = "Manzano Membrilla"
dia = str(3)
mes = str(7)
year = str(1995)
fechanacimiento = dia + "/" + mes + "/" + year
altura = 174
temperatura = float(36.1)
tupla = (nombre, apellidos, fechanacimiento, altura, temperatura)
print("Mi tupla es", tupla)

diccionario = {
"Nombre":nombre,
"Apellidos":apellidos,
"Fecha de nacimiento":fechanacimiento,
"Altura":altura,
"Temperatura":temperatura
}
print("Mi diccionario es",diccionario)