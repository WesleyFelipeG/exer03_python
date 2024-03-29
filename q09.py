lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 6, 3, 7, 8]

elementos_comuns = set(lista1) & set(lista2)

for elemento in elementos_comuns:
    print(elemento)
