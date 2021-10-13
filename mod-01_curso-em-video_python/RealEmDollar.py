# Ler o dinheiro de uma pessoa e dizer quantos dólares ela pode comprar
Real = float(input('Digite sua quantia em real: '))
Dollar = (Real * 0.19300)
print('Você pode comprar $ {:.2f} dollar(es) com R$ {:.2f}' .format(Dollar, Real))