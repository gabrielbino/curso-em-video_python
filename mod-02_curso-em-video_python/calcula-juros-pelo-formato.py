# Calcular o valor a ser pago por um produto, com base na forma de pagamento:
# Á vista: $ ou cheque = 10%OFF
# Á vista no cartão: 5%OFF
# em até 2x no cartão: preço normal
# 3x ou mais: 20% de juros

valorCompra = float(input('Digite o valor da compra: '))
print('FORMAS DE PAGAMENTO')
print('[1] Á vista no dinheiro/cheque')
print('[2] Cartão')
opcao = int(input('Digite a opção escolhida: '))

if opcao == 1:
  valorCompra = valorCompra - (0.1 * valorCompra) # 10%OFF
  print('Você ganhou 10% de desconto! ', end='')
  print(f'O valor da compra é: R$ {valorCompra:.2f}')
elif opcao == 2:
  parcela = int(input('Quantas parcelas? '))
  if parcela == 1:
    valorCompra = valorCompra - (0.05 * valorCompra) # 5%OFF
    print('Você ganhou 5% de desconto! ', end='')
    print(f'O valor da compra é: R$ {valorCompra:.2f}') 
  elif parcela == 2:
    print(f'O valor da compra é {parcela}x de R$ {valorCompra:.2f}') # Preço normal
  else:
    valorCompra = valorCompra + (0.2 * valorCompra) # 20% de juros
    print('Foi atribuído 20% de juros em sua compra.')
    valorJuros = valorCompra / parcela
    print(f'O valor da compra é de {parcela}x de R$ {valorJuros:.2f}')