# Ler vários números e perguntar se quer continuar
# No final, mostrar a média entre todos os números digitados
# e o maior e menor valores lidos.

resp = 's'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
  n = int(input('Digite um número: '))
  soma += n
  quant += 1
  if quant == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
  resp = str(input('Quer continuar? [S/N]: '))
media = soma / quant
print(f'Você digitou {quant} número(s) e a média entre eles é {media}.')