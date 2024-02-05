clientes = []
contas = []
numero_da_conta = 0

def cadastrar_cliente():
        cpf = input("informe seu CPF (formato 12345678900: ")
        # Verifica se o CPF já está cadastrado
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                print("Este CPF já está cadastrado. Apenas um cadastro por CPF é permitido.")
            return
        nome = input("Informe seu nome completo: ")
        nascimento = input("Informe sua data de nascimento:")
        endereco = input("Informe seu endereço residencial: (Rua, bairro, cidade/sigla do estado)")
        clientes.append({"nome": nome, "cpf": cpf, "endereco": endereco, "nascimento": nascimento})

def cadastrar_conta():
    global contas
    global numero_da_conta
    if clientes:
        print("Selecione um cliente para associar a conta:")
        for i, cliente in enumerate(clientes, 1):
              print(f"{i}. {cliente['nome']} - CPF: {cliente['cpf']}")
        escolha_cliente = int(input("Escolha o cliente pelo número: ")) - 1
        
        for conta in contas:
            if conta["cliente"] == clientes[escolha_cliente]:
                print("Este cliente já possui uma conta associada.")
                return

        numero_da_conta += 1

        saldo_inicial = float(input("Digite o saldo inicial da conta: "))
        contas.append({
            "cliente": clientes[escolha_cliente], 
            "saldo": saldo_inicial,
            "agencia": "0001",
            "numero_conta": numero_da_conta
            })
             
        print(f"""
Conta cadastrada com sucesso para o cliente {clientes[escolha_cliente]['nome']}!
Seus dados bancários são Agência: 0001 Conta: {numero_da_conta}""")
    else:
        print("Não há clientes cadastrados. Por favor, cadastre um cliente primeiro.")

    
menu = """
********* MENU *********

[d] Fazer depósito
[s] Realizar saque
[e] Imprimir extrato
[q] Encerrar menu
[c] Cadastrar um novo cliente
[a] Criar nova conta

****** Banco BRB *******
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito():
    global saldo
    global extrato
    deposito_valor = float(input("Digite o valor a ser depositado: "))
    saldo = saldo + deposito_valor
    extrato += f"Depósito de R${deposito_valor}. O saldo atual é de: R${saldo:.2f}. \n"
    return deposito_valor

def saque():
    global saldo
    global extrato
    global numero_saques
    global LIMITE_SAQUES
    if numero_saques < LIMITE_SAQUES:
        saque = float(input("Insira o valor do saque: "))
        if saque > 500 or saque > saldo:
                print("\nO valor inserido sobrepõe ao limite de saque que permitimos ou é maior que o seu saldo atual. \n Por favor, tente novamente")
        elif saque <= 500:
                saldo = saldo - saque
                extrato += f"Saque de R${saque}. O saldo atual é de: R${saldo:.2f}. \n"
                print(f"Saque de R${saque} realizado com sucesso. O saldo atual é de: R${saldo:.2f}.")
                numero_saques +=1
    else:
        print("Você excedeu o seu número de saques diário! :) \n Por favor, volte amanhã.")
        extrato += "Limite de saques atingido. \n"

def imprimir_extrato():
    global extrato
    print(f"{extrato}\n\n>>> Saldo final: {saldo:.2f}")
        

while True:
    opcao = input(f"{menu}Digite a letra da operação: \n")
    if opcao == "d":
        deposito_valor = deposito()
        print(f"Depósito de R${deposito_valor} realizado com sucesso. O saldo atual é de: R${saldo:.2f}.")
    elif opcao == "s":
       saque()
    elif opcao == "e":
        imprimir_extrato()
        resposta = input("Você deseja continuar? (s/n): ")
        if resposta == "s":
            continue
        elif resposta == "n":
            break
        else:
            print("Reposta inválida, por favor digite s ou n.")
    elif opcao == "c":
        cadastrar_cliente()
    elif opcao == "a":
        cadastrar_conta()
    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")