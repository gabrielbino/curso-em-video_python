# ler um valor e mostrar a tabuada
# quando o número for negativo, break.

print('=== Multiplicação ===')
n = int(input('Digite um número: '))
cont = 0
while cont < 10:
  cont += 1
  print(f'{n} x {cont:2} = {n*cont}')