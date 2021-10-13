salario = float(input('Digite o valor do salário mensal atual: '))
aumento = float(input('Digite a porcentagem do aumento (sem o %): '))
salarioComAumento = ((aumento / 100) * salario) + salario
print('Seu salário atual é de: R$ {:.2f}' .format(salarioComAumento))
