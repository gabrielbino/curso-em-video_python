# ler a idade e o sexo de várias pessoas, perguntando se quer ou não
# continuar. No final, mostrar Quantos tem mais de 18 anos.
# quantos homens tem cadastrado e quantas mulheres tem menos de 20 anos.

cad = True
saida = 's'
while cad != False:
  while saida not in 'Nn':
    print('=== Cadastro de pessoas ===')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))
    saida = str('Quer continuar? [S/N]: ')
