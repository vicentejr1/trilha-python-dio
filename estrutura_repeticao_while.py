opcao = -1

while opcao != 0:

    opcao = int(input("\nEscolha uma opção: \n[1] Sacar \n[2] Extrato \n[0] Sair \n\nDigite aqui:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

print("\nSaindo do programa!")