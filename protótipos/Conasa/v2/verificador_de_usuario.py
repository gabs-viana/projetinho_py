import tkinter as tk
from tkinter import messagebox

def obter_nomes():
  nome = nome_entry.get()
  palavras_nome = nome.split()
  primeiro_nome = palavras_nome[0].lower()
  ultimo_nome = palavras_nome[-1].lower()
  return primeiro_nome, ultimo_nome

def imprimir_dados_email():
  primeiro_nome, ultimo_nome = obter_nomes()
  email_info = f"""Certo, então os respectivos dados são:
Email: {primeiro_nome}.{ultimo_nome}@conasa.com
Senha = Conas@202!\n"""
  with open('dados.txt', 'w') as f:
    f.write(email_info)

def imprimir_aplicativos():
  app_info = """\nAplicativos:
- JAVA, 
- Chrome, 
- 7ZIP, 
- Adobe Acrobat Reader (sem McAfee), 
- Teams Corporativo, 
- Pacote Office *fazer login no Outlook e Teams, 
- Vivo Telefone, 
- Kapersky"""
  with open('dados.txt', 'a') as f:
    f.write(app_info)

def verificar_protheus():
  protheus = protheus_var.get()
  if protheus.lower() == "sim":
    with open('dados.txt', 'a') as f:
      f.write("\n- Necessário Protheus")

def verificar_andar():
  andar = andar_var.get()
  if andar == "5":
    impressora_info = "\n\nVerificar precisão das impressoras:\n - 192.168.10.3/Color\n - 192.168.10.4/Black and white"
  elif andar == "7":
    impressora_info = "\n\nVerificar precisão das impressoras:\n - 192.168.10.7/Black and white\n - 192.168.10.8/Color"
  with open('dados.txt', 'a') as f:
    f.write(impressora_info)

def verificar_vpn():
  vpn = vpn_var.get()
  if vpn.lower() == "sim":
    with open('dados.txt', 'a') as f:
      f.write("\n- Necessário VPN")

def gerar_dados():
  imprimir_dados_email()
  imprimir_aplicativos()
  verificar_protheus()
  verificar_vpn()
  verificar_andar()
  messagebox.showinfo("Dados Gerados", "Os dados foram gerados e salvos no arquivo 'dados.txt'.")

root = tk.Tk()

nome_label = tk.Label(root, text="Nome do novo funcionário:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

root.geometry("300x600")

protheus_var = tk.StringVar()
protheus_check = tk.Checkbutton(root, text="Usa Protheus?", variable=protheus_var, onvalue="sim", offvalue="não")
protheus_check.pack()

andar_var = tk.StringVar()
andar_radio5 = tk.Radiobutton(root, text="5° andar", variable=andar_var, value="5")
andar_radio5.pack()
andar_radio7 = tk.Radiobutton(root, text="7° andar", variable=andar_var, value="7")
andar_radio7.pack()

vpn_var = tk.StringVar()
vpn_check = tk.Checkbutton(root, text="É necessário VPN?", variable=vpn_var, onvalue="sim", offvalue="não")
vpn_check.pack()

botao = tk.Button(root, text="OK", command=gerar_dados)
botao.pack()

root.mainloop()