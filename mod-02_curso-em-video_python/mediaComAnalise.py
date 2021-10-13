# Média aritmética
# Solicitar duas notas do usuário, calcular a média e dizer:
# média < 5 = reprovado | média entre 5 e 6.9 = recuperação | >= 7 = aprovado

n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
media = (n1 + n2) / 2

if media >= 7:
  print('Você foi aprovado!')
  print(f'Sua nota final foi: {media}')
elif 7 > media >= 5:
  print('Você está de recuperação.')
  print(f'Sua nota final foi: {media}')
else:
  print('Você foi reprovado. Não desista, ano que vem pode ser melhor!')
  print(f'Sua nota final foi: {media}')