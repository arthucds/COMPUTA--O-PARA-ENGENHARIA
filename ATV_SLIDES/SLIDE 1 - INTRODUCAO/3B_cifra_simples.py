# Exercícios 3 | Strings

# B - CIFRA SIMPLES
# -----------------
# EXEMPLO
# Digite uma palavra: abacaxi
# A palavra cifrada é: ibicixu

palavra = input('Digite uma palavra: ')
cifrada = palavra.replace('a', 'i').replace('e', 'o')

print(f"A palavra cifrada é {cifrada}")