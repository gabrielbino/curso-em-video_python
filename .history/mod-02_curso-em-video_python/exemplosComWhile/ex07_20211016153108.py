# ler um número e mostrar os n primeiros elementos
# em uma sequência de fibonacci.

print('='*25)
print('Sequência de Fibonacci')
print('='*25)
quantidadeTermos = int(input('Digite quantos termos serão exibidos: '))
termo1 = 0
termo2 = 1
print(f'{termo1} -- {termo2}', end='')
cont = 3
while cont <= quantidadeTermos:
  termo3 = termo1 + termo2
  print(f' -- {termo3}', end='')
  termo1 = termo2
  termo2 = termo3
  cont += 1
print(' -- FIM!')

