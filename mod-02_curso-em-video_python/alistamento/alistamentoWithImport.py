from datetime import date

atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc

print(f'Você tem {idade} ano(s) de idade')

if idade == 18:
  print('Está na hora de se alistar!')
elif idade > 18:
  maiorQ = idade - 18
  print(f'Passou {maiorQ} ano(s) desde o seu alistamento! (Se é que você se alistou...)')
  print(f'O ano do seu alistamento foi em: {atual - maiorQ}')
else:
  menorQ = 18 - idade
  print(f'Ainda falta(m) {menorQ} ano(s) para você se alistar!')
  print(f'O ano do seu alistamento será em: {atual + menorQ}')