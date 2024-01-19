nome = input("Qual o seu nome completo paizão? ")
# o nome de entrada é "Gabriel Machado Viana"

# Divida o nome em palavras
palavras_nome = nome.split()

# Verifique se há pelo menos duas palavras
if len(palavras_nome) >= 2:
    primeiro_nome = palavras_nome[0]
    ultimo_nome = palavras_nome[-1]
    print(f"Boas vindas {primeiro_nome} {ultimo_nome}!")


