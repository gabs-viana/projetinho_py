def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print (mensagem)

exibir_poema("Segunda-feira, 21 de Janeiro de 2024", "Flamengo", "Olha o que ela faz:", autor="FIU FIU", ano="1981")