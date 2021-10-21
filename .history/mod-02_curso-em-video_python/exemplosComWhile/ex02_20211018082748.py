# jogar par ou ímpar com o computador
# o jogo só será interrompido quando o jogador perder.
# Mostrando o total de vitórias consecutivas.
from random import randint

print('=x= Vamos jogar PAR ou ÍMPAR =x=')
user = str(input('Escolha par ou ímpar [P/I]: ')).strip()[0]
value = int(input('Agora escolha um número de 0 a 10: '))
