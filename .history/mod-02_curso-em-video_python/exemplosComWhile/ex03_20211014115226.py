# Ler dois valores e mostrar um menu na tela
# de 1 a 5, somar, multiplicar, mostrar o maior, novos números
# e sair do programa. Realizar a operação em cada caso.

valor1 = int(input('Digite o 1º número: '))
valor2 = int(input('Digite o 2º número: '))
print('=== Calculadora funcional ===')
print(''' 
[1] somar
[2] multiplicar
[3] maior e menor
[4] novos números
[5] sair do programa.
''')
opcao = int(input('Escolha uma das opções acima: '))

if opcao == 1:
  print(f'{valor1} + {valor2} = {valor1+valor2}')