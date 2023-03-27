def infinite_sequence():
    num = 35.0
    while True:
        yield num
        num += 0.5

lista = []
fin = 42
for i in infinite_sequence():
    if i == fin:
        lista.append(i)
        break
    else:
        lista.append(i)

print(lista)