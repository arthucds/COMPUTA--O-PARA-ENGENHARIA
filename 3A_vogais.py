# Exercícios 3 | Strings

# A - VOGAIS
# ----------
# EXEMPLO
# Digite uma palavra de cinco caracteres: abacaxi
# A palavra contém 4 vogais: a, a, a, i

palavra = input('Digite uma palavra de cinco caracteres: ')
vogais = (letra for letra in palavra if letra.lower() in 'aeiou')

print(f"A palavra contém {len(list(vogais))} vogais: {', '.join([letra for letra in palavra if letra.lower() in 'aeiou'])}")
