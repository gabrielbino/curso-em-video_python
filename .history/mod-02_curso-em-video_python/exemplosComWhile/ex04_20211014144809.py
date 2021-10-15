# Ler um número qualquer e mostrar o seu fatorial.
from math import factorial
print('==== Fatorial ====')
n = int(input('Digite um número: '))
fat = factorial(n)
print(f'O fatorial de {n} é {fat}')