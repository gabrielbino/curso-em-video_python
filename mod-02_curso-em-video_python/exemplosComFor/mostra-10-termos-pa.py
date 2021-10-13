# Lê o 1° termo e a razão de uma P.A.
# No final, mostrar os 10 primeiros termos dessa P.A.

termo1 = int(input('Digite o 1º termo da P.A.: '))
razao = int(input('Digite a razão dessa P.A.: '))
decimoTermo = termo1 + (11 - 1) * razao # enesimo termo de uma P.A.: n = termo1 + (n - 1) * razao

for c in range(termo1, decimoTermo, razao):
  print(c, end=', ')