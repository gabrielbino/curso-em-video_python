# Ler dois números
# Dizer qual deles é maior ou se são iguais.

n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
  print(f'{n1} é maior que {n2}!')
elif n1 < n2:
  print(f'{n2} é maior que {n1}')
else:
  print('Os números são iguais!')
