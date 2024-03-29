def maior_palavra(palavras):
    maior = ""
    for i in palavras:
        if len(i) > len(maior):
            maior = i
    return maior

lis_palavras = ["1", "22", "4444", "333"]
maior_p = maior_palavra(lis_palavras)
print(f"A palavra mais longa é: {maior_p}")