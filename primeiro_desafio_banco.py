print("Sistema Bancário VJ 1.0\n")

menu = f"""
Escolha a Opção desejada:

(1) Sacar
(2) Depositar
(3) Extrato
(4) Sair

"""

saldo = float(0)
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("Saque:\n")
        saque = float(input("Digite o valor do saque: "))

        if saque > 0:
            if saque <= saldo:
                if numero_saques < LIMITE_SAQUES:
                    if saque <= limite:
                        numero_saques += 1
                        saldo -= saque
                        extrato = f"{extrato} \nsaque: R$ {saque:.2f}"
                        print("\nSaque realziado com sucesso!")
                    else:
                        print("\nValor solicitado é maior que o maximo por saque!")
                else:
                    print("\nLimite de saques diários esgotado!")
            else:
                print("\nSaldo insuficiente!")
        else:
            print("Operação falhou! Valor informado é inválido!")
    

    elif opcao == 2:
        print("Deposito:\n")
        deposito = float(input("Digite o valor a ser depositado em R$: "))

        if deposito > 0:
            saldo += deposito
            extrato = f"{extrato} \ndeposito: R$ {deposito:.2f}"
            print("Deposito realizado com sucesso!")
        else:
            print("Operação falhou! Valor informado é inválido!")
    

    elif opcao == 3:
        print("======================= Extrato =======================\n")
        extrato_detalhado = f"Extrato detalhado: \n{extrato} \n\nSaldo atual é: R$ {saldo:.2f}"
        print(f"Não foram realizadas movimentações. \n\nSaldo atual é: R$ {saldo:.2f}" if not extrato else extrato_detalhado)
        print("\n======================================================")


    elif opcao == 4:
        break


    else:
        print("Opção inválida! Digite a opção desejada: ")