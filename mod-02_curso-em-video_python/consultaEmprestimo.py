# Empréstimo bancário para aquisição imobiliária
# Perguntar o Valor da casa, salário do comprador e em quantos anos ele vai pagar
# Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# Caso exceda 30%, o empréstimo será negado

nome = str(input('Qual é o seu nome? '))
print(f'Bem-vindo(a) ao simulador de empréstimo, {nome}!')

valorEmp = float(input('Digite o valor do empréstimo: '))

salario = float(input('Informe aqui o seu salário: '))

tempo = int(input('Em quantos anos planeja quitar essa dívida? '))

dividaPorMes = valorEmp / (tempo * 12)

print(f'Para obter um empréstimo de {valorEmp} em {tempo} anos, a prestação será de {dividaPorMes}')

if dividaPorMes > (.3 * salario):
  print('Infelizmente seu empréstimo não foi aprovado!')
  print('As parcelas excedem o valor mínimo de 30% do valor do seu salário')
else:
  print('Seu empréstimo foi aprovado!')
