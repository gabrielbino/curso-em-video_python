# Ler vários números e perguntar se quer continuar
# No final, mostrar a média entre todos os números digitados
# e o maior e menor valores lidos.

resp = 's'
soma = quant = media = 0
while resp in 'Ss':
  n = int(input('Digite um número: '))
  soma += n
  quant += 1
  resp = str(input('Quer continuar? [S/N]: '))
media = soma / quant
print('Fim!')