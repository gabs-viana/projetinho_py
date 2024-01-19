import ctypes

ctypes.windll.kernel32.SetConsoleIcon.argtypes = [ctypes.c_void_p]
ctypes.windll.kernel32.SetConsoleIcon.restype = ctypes.c_void_p

icon_path = r"C:\Users\gabriel.viana\Downloads\icon.ico"  # Substitua pelo caminho do seu arquivo de ícone
ctypes.windll.kernel32.SetConsoleIcon(ctypes.windll.shell32.ShellExecuteW(0, "open", icon_path, None, None, 1))

import os

def obter_nomes():
    nome = input("Aoba, fala Gabs, qual o nome do novo funcionário? ")
    palavras_nome = nome.split()
    primeiro_nome = palavras_nome[0].lower()
    ultimo_nome = palavras_nome[-1].lower()
    return primeiro_nome, ultimo_nome

def imprimir_dados_email(primeiro_nome, ultimo_nome):
    print(f"""Certo, então os respectivos dados são:
Email: {primeiro_nome}.{ultimo_nome}@conasa.com
Senha = Conas@202!\n""")

def imprimir_aplicativos():
    print("""Aplicativos:
- JAVA, 
- Chrome, 
- 7ZIP, 
- Adobe Acrobat Reader (sem McAfee), 
- Teams Corporativo, 
- Pacote Office *fazer login no Outlook e Teams, 
- Vivo Telefone, 
- Kapersky""")

def verificar_protheus(protheus):
    if protheus.lower() == "sim":
        print("- Necessário Protheus")

def verificar_andar(andar):
    if andar == "5":
        print("\nVerificar precisão das impressoras:\n - 192.168.10.3/Color\n - 192.168.10.4/Black and white")
    elif andar == "7":
        print("\nVerificar precisão das impressoras:\n - 192.168.10.7/Black and white\n - 192.168.10.8/Color")

def verificar_vpn(vpn):
    if vpn.lower() == "sim":
        print("- Necessário VPN")

# Código principal
primeiro_nome, ultimo_nome = obter_nomes()
protheus = input("Usa Protheus? ")
andar = input("5° ou 7° andar? ")
vpn = input("É necessário VPN? \n")

# Limpa o terminal (funciona no Windows)
os.system('cls' if os.name == 'nt' else 'clear')

imprimir_dados_email(primeiro_nome, ultimo_nome)
imprimir_aplicativos()
verificar_protheus(protheus)
verificar_vpn(vpn)
verificar_andar(andar)

# Adicionando entrada do usuário para manter o programa aberto
input("\nPressione Enter para fechar o programa...")