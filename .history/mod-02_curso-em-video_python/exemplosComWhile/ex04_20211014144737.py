# Ler um número qualquer e mostrar o seu fatorial.
from math import fatorial
print('==== Fatorial ====')
n = int(input('Digite um número:'))
fat = fatorial(n)
print(f'O fatorial de {n} é {fat}')