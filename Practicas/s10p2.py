class ListaTemperaturas():

    def __init__(self):
        listatemp = []

    def add(self, tempt):
        listatemp = []
        try:
            listatemp.append(tempt)
        except Exception:
            print("No se puede añadir")

LT = ListaTemperaturas()
LT.add(36.5)
LT.add(45)

for t in LT:
    print(t)