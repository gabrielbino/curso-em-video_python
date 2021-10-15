# Melhore a P.A. anterior, perguntando quantos termos ele quer
# mostrar a mais. Com 0 o programa encerra.

print('=== Gerador de P.A. ===')
termo1 = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
auxiliar = termo1
cont = 1
while cont <= 10:
  print(f'{auxiliar} ; ', end='')
  auxiliar += razao
  cont += 1
print('Quantos termos você quer mostrar a mais? ')