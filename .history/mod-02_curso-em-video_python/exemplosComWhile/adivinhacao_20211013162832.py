# Jogo de adivinhação, só que agora, o jogador vai tentar
# até acertar, depois o programa vai mostrar quantas vezes
# ele tentou até acertar

from random import randint
computador = randint(0, 10)
print('Sou seu computador, escolhi um número entre 0 e 10.')
print('Tente adivinhar!')

acertou = False
while not acertou:
  jogador = int(input('Digite seu palpite: '))
  if jogador == computador:
    acertou = True
print('Você venceu!')


print(f'A máquina escolheu: {computador}')
print(f'Sua escolha foi: {jogador}')

else:
  print('Computador venceu!')