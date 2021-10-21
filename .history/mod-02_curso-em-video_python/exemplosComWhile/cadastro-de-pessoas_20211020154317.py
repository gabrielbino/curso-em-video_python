# ler a idade e o sexo de várias pessoas, perguntando se quer ou não
# continuar. No final, mostrar Quantos tem mais de 18 anos.
# quantos homens tem cadastrado e quantas mulheres tem menos de 20 anos.
sexo = ' '
maiorDe18 = totalHomens = MulherMaiorDe20 = 0
while True:
  print('=== Cadastro de pessoas ===')
  idade = int(input('Digite a idade: '))
  
  if idade >= 18:
    maiorDe18 += 1
  
  while sexo not in 'MF':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().split()[0]
    if sexo == 'M':
      totalHomens += 1
    if sexo == "F":
      if idade < 20:
        MulherMaiorDe20 += 1
  sexo = ' '

  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N]: ')).upper().split()[0]
    if resp == 'N':
      break

print(f'Total de homens: {totalHomens}. Homens maiores de 18 anos: {maiorDe18}.')
print(f'Total de mulheres com mais de 20 anos de idade: {MulherMaiorDe20}.')
