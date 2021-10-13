# Jokenpô
# Perguntar ao usuário qual ele escolhe: Pedra, papel ou tesoura
# A máquina exibe na tela o que ela escolheu e em seguida o resultado.
from random import randint
from time import sleep

print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

jogador = int(input('Digite uma das opções: '))
opcoes = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)

print('PEEDRA')
sleep(1)
print('PAPEEL')
sleep(1)
print('TESOOOURA')
sleep(2)
print('x=' * 14)
print(f'Sua jogada: {opcoes[jogador]}')
print(f'Computador jogou: {opcoes[maquina]}')
print('x=' * 14)

if jogador == 0:
  if maquina == 0:
    print('EMPATE!')
  elif maquina == 1:
    print('Computador venceu!')
  elif maquina == 2:
    print('Você venceu!')

elif jogador == 1:
  if maquina == 0:
    print('Você venceu!')
  elif maquina == 1:
    print('EMPATE!')
  elif maquina == 2:
    print('Computador venceu!')

elif jogador == 2:
  if maquina == 0:
    print('Computador venceu!')
  elif maquina == 1:
    print('Você venceu!')
  elif maquina == 2:
    print('EMPATE!')