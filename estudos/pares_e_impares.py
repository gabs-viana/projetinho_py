numeros = [1, 30, 21, 2, 9, 65, 34]
impares = [numero for numero in numeros if numero % 2 == 1]
pares = [numero for numero in numeros if numero % 2 == 0]
quadrado = [numero ** 2 for numero in numeros]
print(f"""Aqui estão os números impares: {impares} e aqui os números pares: {pares}

Já estes números ao quadrado ficam: {quadrado}

Olha o bobo do número 34: {numeros[-1]}
e o bobalhão do 9: {numeros[4]}""")
pares.append(int((input("Diz outro numero par ai: "))))
teste = pares[-1]
if teste % 2 == 0:
    print(f"Novos pares = {pares}")
else:
    print("Este não é um número par amigão.")