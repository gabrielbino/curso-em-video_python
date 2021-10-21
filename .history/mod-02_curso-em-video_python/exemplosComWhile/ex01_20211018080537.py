# ler um valor e mostrar a tabuada
# quando o número for negativo, break.
from time import sleep

print('=== Multiplicação ===')
cont = 0
resp = 's'
while resp in 'Ss':
  n = int(input('Digite um número inteiro positivo: '))
  if n < 0:
    break
  while cont < 10:
    cont += 1
    print(f'{n} x {cont:2} = {n*cont}')
  print('=x'*25)
  resp = str(input('Quer continuar? [S/N]: '))
  if resp in 'Ss':
    cont = 0
print('Encerrando...')
sleep(1)