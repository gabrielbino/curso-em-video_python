# Ler um número qualquer e mostrar o seu fatorial.

# from math import factorial
print('===== Fatorial =====')
n = int(input('Digite um número: '))
# fat = factorial(n)
c = n
fatorial = 1
print(f'{c}! = ', end='')
while c > 0:
  print(f'{c}', end='')
  print(' x ' if c > 1 else ' = ', end='')
  fatorial *= c
  c -= 1
# print(f'O fatorial de {n} é {fat}')
print(f'{fatorial}')