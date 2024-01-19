from datetime import datetime, timedelta

nome = input("Informe o seu nome: ")
data_nascimento = input("Informe a sua data de nascimento (formato DD/MM/AAAA): ")

# Converte a data de nascimento para um objeto datetime
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

# Obtém a data atual
data_atual = datetime.now()

# Calcula a idade da pessoa
idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

# Verifica se a pessoa já fez aniversário este ano
aniversario_passou = (data_atual.month, data_atual.day) >= (data_nascimento.month, data_nascimento.day)

# Calcula a data exata em que a pessoa pode voltar
ano_volta = data_atual.year + (16 - idade) + int(not aniversario_passou)
data_volta = datetime(ano_volta, data_nascimento.month, data_nascimento.day)

print("Verificando a sua legitimidade...")
if data_atual >= data_volta:
    print("Então você está pronto para tirar carteira, meu bom!")
else:
    print(f"{nome}, volte quando atingir 18 anos. Isso será possível em {data_volta.strftime('%d/%m/%Y')}.")

# base feita pelo Gabs, reestruturação feita pelo mano ChatGPT
