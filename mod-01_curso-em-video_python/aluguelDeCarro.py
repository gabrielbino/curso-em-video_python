""" dia = int(input('Quantos dias você ficou com o carro? '))
valorPorDia = (dia * 60 )
kmRodado = float(input('Quantos Km rodadods? '))
valorPorKm = (kmRodado * .15)
print('O valor a pagar é: R$ {:.2f}' .format((valorPorDia + valorPorKm))) """

# Forma simplificada
dia = int(input('Quantos dias você ficou com o carro? '))
valorPorDia = (dia * 60 )
kmRodado = float(input('Quantos Km rodadods? '))
print('O valor a pagar é: R$ {:.2f}' .format((valorPorDia + (kmRodado * .15))))