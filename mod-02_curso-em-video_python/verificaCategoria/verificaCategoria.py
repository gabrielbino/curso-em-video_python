# Ler o ano de nascimento de um atleta
# e sua categoria de acordo com a idade
# =< 9 MIRIM | 10 a 14 INFANTIL | 15 a 17 JUNIOR | 18 a 20 SÊNIOR | >20 MASTER

nasc = int(input('Digite o seu ano de nascimento: '))
idade = 2021 - nasc

if idade <= 9:
  print('Você está na categoria MIRIM')
elif idade > 9 and idade < 15:
  print('Você está na categoria INFANTIL')
elif idade >= 15 and idade < 18:
  print('Você está na categoria JUNIOR')
elif idade >= 18 and idade <= 20:
  print('Você está na categoria SÊNIOR')
else:
  print('Você está na categoria MASTER')