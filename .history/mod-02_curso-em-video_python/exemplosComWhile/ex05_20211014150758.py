# Refaça a P.A. usando while.
# ler o 1º termo e a razao e mostrar os 10 primeiros termos.

print('=== Gerador de P.A. ===')
termo1 = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
auxiliar = termo1
cont = 1
while cont <= 10:
  print(f'{auxiliar} ; ', end='')
  auxiliar += razao
  cont += 1