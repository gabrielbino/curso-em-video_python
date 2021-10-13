# Ler a data de nascimento de 7 pessoas e dizer quantas ainda
# não atingiram maioridade e quantas são maiores.
# Maioridade = 21 anos
from datetime import date

anoAtual = date.today().year
maioridade = 0
menorDeIdade = 0
for c in range(0, 7):
  nasc = int(input('Digite o seu ano de nascimento: '))
  if (anoAtual - nasc) >= 21:
    maioridade += 1
  else:
    menorDeIdade += 1
print(f'{maioridade} pessoa(s) atingiram a maioridade.')
print(f'{menorDeIdade} pessoa(s) não atingiram a maioridade.')
