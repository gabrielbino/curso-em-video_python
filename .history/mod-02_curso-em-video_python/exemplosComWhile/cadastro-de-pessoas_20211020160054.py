# ler a idade e o sexo de várias pessoas, perguntando se quer ou não
# continuar. No final, mostrar Quantos tem mais de 18 anos.
# quantos homens tem cadastrado e quantas mulheres tem menos de 20 anos.

teste = True
sexo = ' '
totalMen = maior18 = menosDe20 = 0
print('=== Cadastro de pessoas ===')
while teste == True:
  idade = int(input('Digite a idade: '))
  
  while sexo not in 'MF':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().split()[0]

  if sexo == 'M':
    totalMen += 1
    if idade > 18:
      maior18 += 1
  elif sexo == 'F':
    if idade < 20:
      menosDe20 += 1
  
  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N]: ')).upper().split()[0]
    if resp == 'N':
      teste = False

print(f'Total de homens: {totalMen}')
print(f'Homens maiores de 18 anos: {maior18}')
print(f'Mulheres menores de 20 anos: {menosDe20}')
