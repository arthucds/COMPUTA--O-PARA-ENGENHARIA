# Exercícios 3 | Strings

# D - SUBNÚMERO
# -------------
# EXEMPLOS
# Digite a sequência p: 123
# Digite a sequência q: 123456
# A sequência p aparece dentro de q.

p = input("Digite a sequência p: ")
q = input("Digite a sequência q: ")

if p in q:
    print("A sequência p aparece dentro de q.")

else:
    print("A sequência p não aparece dentro de q.")