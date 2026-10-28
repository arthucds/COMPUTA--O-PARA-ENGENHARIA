# Exercícios 2 | Decisões

# D - TARIFA REVISADA
# -------------------
# EXEMPLO
# Digite a quilometragem percorrida: 0
# O valor a pagar é de R$ 30.00

# Digite a quilometragem percorrida: 50
# O valor a pagar é de R$ 30.00

# Digite a quilometragem percorrida: 150
# O valor a pagar é de R$ 30.00

# Digite a quilometragem percorrida: 300
# O valor a pagar é de R$ 30.00

quilometragem = float(input('Digite a quilometragem percorrida: '))

if quilometragem <= 300:
    valor_a_pagar = 30.00
    print(f'O valor a pagar é de R$ {valor_a_pagar:.2f}')

else:
    valor_a_pagar = quilometragem * 0.05
    print(f'O valor a pagar é de R$ {valor_a_pagar:.2f}')