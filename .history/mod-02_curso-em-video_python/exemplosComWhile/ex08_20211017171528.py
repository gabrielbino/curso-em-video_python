# Ler números inteiros até o usuário digitar 999.
# Mostar a soma deles e quantos foram digitados,
# desconsiderando o 999.
n = cont = soma = 0
while n != 999:
  n = int(input('Digite um número [999 para sair]: '))
  cont += 1
print(f'Você digitou {cont} número(s).')