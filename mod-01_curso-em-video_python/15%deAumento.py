# Ler o salário
# Dizer quanto é com um aumento de 15%

""" salario = float(input('Qual o seu salário mensal atual? '))
aumento = float(salario * .15)
valorAtual = float(salario + aumento)
print('Com um aumento de (15%) seu salário foi para: R$ {:.2f}' .format(valorAtual)) """

# Forma simplificada
salario = float(input('Qual o seu salário mensal atual? '))
valorAtual = salario + (salario * .15)
print('Com um aumento de (15%) seu salário foi para: R$ {:.2f}' .format(valorAtual))