# Ler o ano de nascimento do usuário
# Dizer se ele ainda vai ser alistar, se já é a hora ou se já passou
# Se já passou o tempo ou ainda não, informar quanto tempo

nasc = int(input('Digite o seu ano de nascimento: '))
idade = 2021 - nasc

if idade == 18:
  print('Está na hora de se alistar!')
elif idade > 18:
  maiorQ = idade - 18
  print(f'Passou {maiorQ} ano(s) do ano de seu alistamento!')
else:
  menorQ = 18 - idade
  print(f'Ainda falta(m) {menorQ} ano(s) para você se alistar!')