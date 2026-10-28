# Exercícios 2 | Decisões

# B - CLASSIFICADOR
# -----------------
# EXEMPLOS
# Digite um número: 22
# O número 22 é positivo e par.

# Digite um número: 21
# O número 21 é positivo e ímpar.

# Digite um número: -9
# O número -9 é negativo.

# Digite um número: 0
# O número digitado é zero.

numero = int(input('Digite um número: '))

if numero > 0 and numero  % 2 == 0:
    print(f'O número {numero} é positivo e par.')

elif numero > 0 and numero % 2 != 0:
    print(f'O número {numero} é positivo e ímpar.')

if numero < 0 and numero % 2 == 0:
    print(f'O número {numero} é negativo e par.')

elif numero < 0 and numero % 2 != 0:
    print(f'O número {numero} é negativo e ímpar.')

else:
    print(f'O número digitado é zero.')