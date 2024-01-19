resposta = input("\nO que você quer aprender hoje?: \n\n 1)Passiva do Sett \n 2)habilidade Q \n 3)Habilidade W \n 4)Habilidade E \n 5)Habilidade Ultimate(R) \n\n Escolha um número de 1 à 5: ")

if resposta == "1":
    print("Nome: Ousadia da Arena \nDescrição: Os ataques básicos de Sett alternam entre socos de direita e esquerda. Socos de direita são levemente mais fortes e rápidos. Como Sett odeia perder, recebe Regeneração de Vida adicional com base na Vida perdida.")
elif resposta == "2":
    print("Nome: Pancadaria \nDescrição: Os próximos dois ataques de Sett causam dano adicional com base na Vida máxima do alvo. Ele também recebe Velocidade de Movimento enquanto se move em direção a Campeões inimigos.")
elif resposta == "3":
    print("Nome: Casca-grossa \nDescrição: O dano que Sett sofre é armazenado passivamente como Ousadia. Ao conjurar a habilidade, Sett consome toda a Ousadia armazenada em troca de um escudo e desfere um soco em uma área, causando Dano Verdadeiro no centro e Dano Físico nas laterais.")
elif resposta == "4":
    print("Nome: Quebra-crânio \nDescrição:  Sett puxa todos os inimigos de cada lado seu, causando dano e atordoando. Caso haja inimigos somente de um lado, eles sofrem redução de velocidade em vez de atordoamento.")
elif resposta == "5":
    print("Nome: Hora do Show \nDescrição: Sett carrega um Campeão inimigo pelos ares e o arremessa no chão, causando dano e redução de velocidade a todos os inimigos que estiverem próximos ao local de aterrissagem.")

outroChamp = input("\nVocê deseja verificar outro campeão? ")

if outroChamp == "Sim":
    print("\nSelecione o campeão")
else:
    print("\nOk, é nois")