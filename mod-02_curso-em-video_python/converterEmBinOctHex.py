# Ler um número inteiro
# Pedir ao usuário para informar qual será a base a de conversão
# 1 para binário, 2 para octal, 3 para hexadecimal

n = int(input('Digite um número inteiro: '))
print('''Digite
[1] para converter em binário
[2] para converter em octal
[3] para converter em hexadecimal''')
userEscolha = int(input('Sua opção: '))

if userEscolha == 1:
  print(f'A conversão de {n} em binário é: {bin(n)[2:]}') # converter inteiro em binário
elif userEscolha == 2:
  print(f'A conversão de {n} em octal  é: {oct(n)[2:]}') # converter inteiro em octal
elif userEscolha == 3:
  print(f'A conversão de {n} em hexadecimal é: {hex(n)[2:]}') # converter inteiro em hexadecimal
else:
  print('Opção inválida!')