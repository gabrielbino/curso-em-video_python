# Ler dois valores e mostrar um menu na tela
# de 1 a 5, somar, multiplicar, mostrar o maior, novos números
# e sair do programa. Realizar a operação em cada caso.
from time import sleep

print('=== Calculadora funcional ===')
valor1 = int(input('Digite o 1º número: '))
valor2 = int(input('Digite o 2º número: '))

opcao = 0
while opcao != 5:
  print('[1] somar')
  print('[2] multiplicar')
  print('[3] maior e menor')
  print('[4] novos números')
  print('[5] sair do programa.')
  opcao = int(input('Escolha uma das opções acima: '))
  if opcao == 1:
    print(f'{valor1} + {valor2} = {valor1+valor2}')
  elif opcao == 2:
    print(f'{valor1} x {valor2} = {valor1*valor2}')
  elif opcao == 3:
    if valor1 == valor2:
      print(f'Os números {valor1} e {valor2} são iguais.')
    elif valor1 > valor2:
      print(f'{valor1} é o maior número digitado. {valor2} é o menor.')
    else:
      print(f'{valor2} é o maior número digitado. {valor1} é o menor.')
  elif opcao == 4:
    print('Informe os números novamente:')
    valor1 = int(input('Digite o 1º número: '))
    valor2 = int(input('Digite o 2º número: '))
  elif opcao == 5:
    print('Encerrando...')
    sleep(1)
  else:
    print('Opção inválida.')