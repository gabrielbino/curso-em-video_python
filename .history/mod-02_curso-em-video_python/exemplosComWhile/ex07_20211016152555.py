# ler um número e mostrar os n primeiros elementos
# em uma sequência de fibonacci.

print('='*25)
print('Sequência de Fibonacci')
print('='*25)
quant = int(input('Digite quantos termos serão exibidos: '))
termo1 = 0
termo2 = 1
print(f'{termo1} -- {termo2}', end='')
termo3 = termo1 + termo2
print(f'-- {termo3}', end='')