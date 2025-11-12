#"python"

frase = input("Digite uma frase: ")
frase_minuscula = frase.lower()
VOGAIS = "aeiou"


# usando iterável
for letra in frase_minuscula:
    if letra in VOGAIS:
        print(letra, end=" ")
print()

# função built-in range
for numero in range(0, 101, 5):
    print(numero, end=" ")
