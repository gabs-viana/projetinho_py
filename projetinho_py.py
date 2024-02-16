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
        print(f"Cliente com o CPF {cpf} cadastrado com sucesso! Agora é só criar a conta ;)")

def cadastrar_conta():
    global contas
    global numero_da_conta
    global saldo
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
        saldo += saldo_inicial
             
        print(f"""
Conta cadastrada com sucesso para o cliente {clientes[escolha_cliente]['nome']}!
Seus dados bancários são Agência: 0001 Conta: {numero_da_conta}""")
    else:
        print("Não há clientes cadastrados. Por favor, cadastre um cliente primeiro.")

    
menu = """
********* MENU *********

Área do usuário -
[c] Cadastrar um novo cliente
[a] Criar nova conta

Transações -
[d] Fazer depósito
[s] Realizar saque
[e] Imprimir extrato
[q] Encerrar menu


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
    if clientes and contas:
        deposito_valor = float(input("Digite o valor a ser depositado: "))
        saldo = saldo + deposito_valor
        extrato += f"Depósito de R${deposito_valor}. O saldo atual é de: R${saldo:.2f}. \n"
        return deposito_valor
        print(f"Depósito de R${deposito_valor} realizado com sucesso. O saldo atual é de: R${saldo:.2f}.")
    else:
        print("Você não possui uma conta para fazer o depósito, por favor, crie uma conta primeiro.")
        return None

def saque():
    global saldo
    global extrato
    global numero_saques
    global LIMITE_SAQUES
    if clientes and contas:
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
    else: 
        print("Você não possui uma conta para fazer saques, por favor, crie uma conta primeiro.")
        return None

def imprimir_extrato():
    global extrato
    if clientes and contas:
        print(f"{extrato}\n\n>>> Saldo final: {saldo:.2f}")
        return True
    else:
        print("Você não possui uma conta para imprimir um extrato, por favor, crie uma conta primeiro.")
        return False

while True:
    opcao = input(f"{menu}Digite a letra da operação: \n")
    if opcao == "d":
        deposito_valor = deposito()
    elif opcao == "s":
       saque()
    elif opcao == "e":
        if imprimir_extrato():
            resposta = input("Você deseja continuar? (s/n): ")
            if resposta == "s":
                continue
            elif resposta == "n":
                break
            else:
                print("Resposta inválida, por favor digite 's' para continuar ou 'n' para sair.")
                continue
        else:
            pass
    elif opcao == "c":
        cadastrar_cliente()
    elif opcao == "a":
        cadastrar_conta()
    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")