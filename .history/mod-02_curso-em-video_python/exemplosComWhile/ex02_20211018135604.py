# jogar par ou ímpar com o computador
# o jogo só será interrompido quando o jogador perder.
# Mostrando o total de vitórias consecutivas.
from random import randint

while True:
  print('=x= Vamos jogar PAR ou ÍMPAR =x=')
  number = int(input('Escolha um número: '))
  computer = randint(0, 10)
  total = number + computer
  userEscolha = ' '
  while userEscolha not in 'PI':
    userEscolha = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()[0]
  print(f'Você jogou {number} e o computador jogou {computer}')
  print(f'O total foi {total}')
  if userEscolha == 'P':
    if total % 2 == 0:
      print('Você venceu!')
    else:
      print('Computador venceu!')
      break
  if userEscolha == 'I':
    if total % 2 == 0:
      print('Computador venceu!')
      break
    else:
      print('Você venceu!')
