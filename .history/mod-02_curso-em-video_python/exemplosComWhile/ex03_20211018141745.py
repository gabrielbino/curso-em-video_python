# ler a idade e o sexo de várias pessoas, perguntando se quer ou não
# continuar. No final, mostrar Quantos tem mais de 18 anos.
# quantos homens tem cadastrado e quantas mulheres tem menos de 20 anos.

resp = ' '
sexo = ' '
maiorDe18 = totalHomens = 0
while resp not in 'N':
  print('=== Cadastro de pessoas ===')
  idade = int(input('Digite a idade: '))
  if idade >= 18:
    maiorDe18 += 1
  while sexo not in 'MF':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().split()[0]
    if sexo == 'M':
      totalHomens += 1

  resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
