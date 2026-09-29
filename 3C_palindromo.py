# Exercícios 3 | Strings

# C - PALÍNDROMO
# --------------
# EXEMPLOS
# Digite um texto: A grama é amarga
# É um palíndromo!

# Digite um texto: escola
# Não é um palíndromo!

texto = input("Digite um texto: ")
texto_limpo = texto.replace(" ", "").lower()

if texto_limpo == texto_limpo[::-1]:
    print("É um palíndromo!")

else:
    print("Não é um palíndromo!")