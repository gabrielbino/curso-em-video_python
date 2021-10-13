# Ler um número inteiro e dizer se ele é ou não um nº primo.

n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
  if n % c == 0:
    print('\033[33m', end='') # Amarelo
    total += 1
  else:
    print('\033[31m', end='')
  print(f'{c}', end=' ')
print(f'\nO número {n} foi divisível {total} vezes. ', end='')
if total == 2:
  print('Por isso ele é PRIMO.')
else:
  print('Por isso ele é NÃO é primo.')
