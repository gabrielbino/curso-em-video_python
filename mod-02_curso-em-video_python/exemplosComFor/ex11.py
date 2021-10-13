# Ler o nome, idade sexo de cada pessoa e mostrar:
# A média da idade de grupo, o nome do mais velho e
# quantas mulheres tem menos de 20 anos.

somaIdade = 0
mediaIdade = 0
maisVelho = 0
nomeMaisVelho = 0
mulherMenorDe20 = 0
for p in range(1, 5):
  print(f'---- {p}º PESSOA ----')
  nome = str(input('Digite o nome: '))
  idade = int(input('Digite a idade: '))
  sexo = str(input('Digite o sexo [M/F]: '))
  somaIdade += idade
  if p == 1 and sexo in 'Mm': # sexo in 'Mm' permite analisar as duas letras, diferente de ==, que só iria analisar uma ou outra.
    maisVelho = idade
    nomeMaisVelho = nome
  if sexo in 'Mm' and idade > maisVelho:
    maisVelho = idade
    nomeMaisVelho = nome
  if sexo in 'Mm' and idade < 20:
    mulherMenorDe20 += 1
mediaIdade = somaIdade / 4
print(f'A média da idade do grupo é {mediaIdade} anos.')
print(f'O homem mais velho do grupo é {nomeMaisVelho} com {maisVelho} anos.')
print(f'Ao todo são {mulherMenorDe20} mulher(es) com menos de 20 anos.')