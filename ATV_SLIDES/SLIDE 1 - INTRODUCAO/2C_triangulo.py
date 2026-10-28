# Exercícios 2 | Decisões

# C - TRIÂNGULO
# -------------
# EXEMPLO
# Lado 1: 3
# Lado 2: 4
# Lado 3: 5
# O triângulo é válido e sua área é 6.0.

from math import sqrt

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2  # Semiperimetro
    area = sqrt(s * (s - a) * (s - b) * (s - c))  # Área de Heron
    print(f'O triângulo é válido e sua área é {area:.1f}.')

else:
    print('O triângulo não é válido.')