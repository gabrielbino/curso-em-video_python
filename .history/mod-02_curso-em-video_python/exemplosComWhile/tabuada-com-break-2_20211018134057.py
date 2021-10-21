while True:
  print('=== Multiplicação ===')
  n = int(input('Escolha o número: '))
  if n < 0:
    print('Números negativos encerram o programa.')
    break
  for cont in range(1, 11):
    print(f'{n:2} x {cont} = {n*cont}')
print('Operação finalizada.')