# ler um valor e mostrar a tabuada
# quando o número for negativo, break.

print('=== Multiplicação ===')
cont = 0
resp = 's'
while resp in 'Ss':
  n = int(input('Digite um número: '))
  while cont < 10:
    if n < 0:
      break
    cont += 1
    print(f'{n} x {cont:2} = {n*cont}')
  print('=x'*25)
  resp = str(input('Quer continuar? [S/N]: '))
  if resp in 'Ss':
    cont = 0