# Exercícios 2 | Decisões

# A - MAIOR E INTERMEDIÁRIO
# -------------------------
# EXEMPLO
# Número 1: 21
# Número 2: 9
# Número 3: 6
# 6 é o maior número e 9 é o valor do meio.

numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))
numero3 = int(input('Número 3: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'{numero1} é o maior número e {max(numero2, numero3)} é o valor do meio.')

elif numero2 > numero1 and numero2 > numero3:
    print(f'{numero2} é o maior número e {max(numero1, numero3)} é o valor do meio.')

elif numero3 > numero1 and numero3 > numero2:
    print(f'{numero3} é o maior número e {max(numero1, numero2)} é o valor do meio.')