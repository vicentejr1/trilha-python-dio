MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, você pode tirar o CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar o CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, você pode tirar o CNH.")
else:
    print("Ainda não pode tirar o CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, você pode tirar o CNH.")
elif idade == IDADE_ESPECIAL:
    print("Você pode fazer as aulas teóricas, mas não as práticas.")
else:
    print("Ainda não pode tirar o CNH.")