from datetime import date

atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc

if idade <= 9:
  print(f'O atleta tem {idade} ano(s) de idade.')
  print('Está na categoria: MIRIM.')
elif 9 < idade < 15:
  print(f'O atleta tem {idade} ano(s) de idade.')
  print('Está na categoria: INFANTIL.')
elif 14 < idade < 18:
  print(f'O atleta tem {idade} ano(s) de idade.')
  print('Está na categoria: JUNIOR.')
elif 17 < idade <= 20:
  print(f'O atleta tem {idade} ano(s) de idade.')
  print('Está na categoria: SÊNIOR.')
else:
  print(f'O atleta tem {idade} ano(s) de idade.')
  print('Está na categoria: MASTER.')