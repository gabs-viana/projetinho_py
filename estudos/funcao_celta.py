def carro(modelo="", ano="", placa="", marca="", motor="", combustivel=""):
          return f"O carro é um {modelo} da {marca}, ano {ano}, placa {placa}, motor {motor} e usa {combustivel} como combustível."

carro1 = carro(modelo="Celta", ano ="2005", placa="HBU-8371", marca="Chevrolet", motor="1.0", combustivel="Gasolina")

print(carro1)