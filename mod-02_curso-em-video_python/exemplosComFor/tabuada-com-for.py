# Refazer o desafio da tabuada de um nº que o usuário escolher
# usando FOR

n = int(input('Digite um número: '))
for c in range(1, 11):
  print(f'{n} x {c:2} = {n*c}')