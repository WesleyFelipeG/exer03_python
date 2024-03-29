palavras = ["AAAAA", "BBBBB", "AAABB", "BBBAA"]

print(palavras)

contador = 0
for i in palavras:
    if i.startswith('A'):
        contador += 1

print(f"Palavras que começam com 'A': {contador}")
