valores = list(range(10, 60, 10))

print("Lista de valores:", valores)

soma = 0
for i in valores:
    soma += i

media = soma / len(valores)

print(f"Média: {media}")
