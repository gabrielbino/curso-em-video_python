# Jogo de adivinhação, só que agora, o jogador vai tentar
# até acertar, depois o programa vai mostrar quantas vezes
# ele tentou até acertar

from random import randint
computador = randint(0, 10)
jogador = int(input('Digite um número de 0 a 10: '))

print(f'A máquina escolheu: {computador}')
print(f'Sua escolha foi: {jogador}')
if jogador == computador:
  print('Você venceu!')
else:
  print('Computador venceu!')