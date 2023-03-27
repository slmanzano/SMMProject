class EnumeracionDepartamento():
    tesoreria = 1
    financiero = 2
    administracion = 3
    informatica = 4
    logistica = 5
    direccion = 6

    def listar(self):
        contador = 1
        for nombre in self:
            print(contador, nombre)
            contador += 1

departamentos = EnumeracionDepartamento();


class ClasePersona():
    Nombre = ""
    Edad = 0

    def __init__(self,nombre,edad):
        self.Nombre = nombre
        self.Edad = edad

    def saludos(self):
        print(self.Nombre + " " + str(self.Edad))


persona1 = ClasePersona("Luis Martin", 40)

class ClaseTrabajador():
    Codigo = ""
    Salario = 0

    def __init__(self,codigo,salario):
        self.Codigo = codigo
        self.Salario = salario

    def muestra(self):
        print(self.Codigo + " " + str(self.Salario))

trabajador1 = ClaseTrabajador("TRD", 35000)