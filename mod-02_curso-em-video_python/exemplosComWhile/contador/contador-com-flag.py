# Ler números inteiros até o usuário digitar 999.
# Mostar a soma deles e quantos foram digitados,
# desconsiderando o 999.
n = cont = soma = 0
n = int(input('Digite um número [999 para sair]: '))
while n != 999:
  soma += n
  cont += 1
  n = int(input('Digite um número [999 para sair]: '))
print(f'Você digitou {cont} número(s) e a soma entre eles foi {soma}.')