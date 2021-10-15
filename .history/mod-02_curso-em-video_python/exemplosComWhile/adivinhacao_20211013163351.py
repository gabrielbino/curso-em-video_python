# Jogo de adivinhação, só que agora, o jogador vai tentar
# até acertar, depois o programa vai mostrar quantas vezes
# ele tentou até acertar

from random import randint
computador = randint(0, 10)
print('Sou seu computador, escolhi um número entre 0 e 10.')
print('Tente adivinhar!')

acertou = False
palpites = 0
while not acertou:
  jogador = int(input('Digite seu palpite: '))
  palpites += 1
  if jogador == computador:
    acertou = True
  else:
    if jogador < computador:
      print('Mais... Tente mais uma vez.')
    elif jogador > computador:
      print('Menos... Tente mais uma vez.')
print(f'Você venceu! {palpites} tentativas. Parabéns!')