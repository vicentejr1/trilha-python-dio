nome = "Vicente"
idade = 26
saldo = 45.435


cpf = "09726384400" #format
print("O seu CPF: {}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]))

dados = {"nome": "Vicente", "idade": 26} #format com dicionário
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f   }")