# Melhore a P.A. anterior, perguntando quantos termos ele quer
# mostrar a mais. Com 0 o programa encerra.
from time import sleep

print('=== Gerador de P.A. ===')
termo1 = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
auxiliar = termo1
cont = 1
total = 0
mais = 10
while mais != 0:
  total += mais
  while cont <= total:
    print(f'{auxiliar} ; ', end='')
    auxiliar += razao
    cont += 1
  print('Prontinho!')
  mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Encerrando...')
sleep(1)