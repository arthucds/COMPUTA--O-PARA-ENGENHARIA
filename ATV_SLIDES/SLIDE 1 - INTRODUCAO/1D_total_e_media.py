# Exercícios 1 | Fundamentos

# D - TOTAL E MÉDIA
# -----------------
# EXEMPLO
# Valor da medida 1: 10
# Valor da medida 2: 20
# Valor da medida 3: 30
# Total: 60.00
# Média: 20.00

medida1 = float(input('Valor da medida 1: '))
medida2 = float(input('Valor da medida 2: '))
medida3 = float(input('Valor da medida 3: '))

total = medida1 + medida2 + medida3
media = total / 3

print(f'Total: {total:.2f}')
print(f'Média: {media:.2f}')