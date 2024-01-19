menu = """
********* MENU *********

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

while True:

    opcao = input(f"{menu}Digite a letra da operação: \n")

    if opcao == "d":
        deposito = float(input("Digite o valor a ser depositado: "))
        saldo = saldo + deposito
        extrato += f"Depósito de R${deposito}. O saldo atual é de: R${saldo:.2f}. \n"
        print(f"Depósito de R${deposito} realizado com sucesso. O saldo atual é de: R${saldo:.2f}.")
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Insira o valor do saque: "))
            if saque > 500 or saque > saldo:
                print("O valor inserido sobrepõe ao limite de saque que permitimos ou é maior que o seu saldo atual. \n Por favor, tente novamente")
            elif saque <= 500:
                saldo = saldo - saque
                extrato += f"Saque de R${saque}. O saldo atual é de: R${saldo:.2f}. \n"
                print(f"Saque de R${saque} realizado com sucesso. O saldo atual é de: R${saldo:.2f}.")
                numero_saques +=1
        elif numero_saques >= LIMITE_SAQUES:
            print("Você excedeu o seu número de saques diário! :) \n Por favor, volte amanhã.")
            extrato += "Limite de saques atingido. \n"
    elif opcao == "e":
        print(f"{extrato}\n\n>>> Saldo final: {saldo:.2f}")
        resposta = input("Você deseja continuar? (s/n): ")
        if resposta == "s":
            continue
        elif resposta == "n":
            break
        else:
            print("Reposta inválida, por favor digite s ou n.")
    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")