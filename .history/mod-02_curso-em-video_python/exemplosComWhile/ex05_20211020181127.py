# simular um caixa eletrônico. perguntar qual valor será sacado (int)
# Informar quantas cédulas serão entregues.
# Considere que o caixa tem: 50 , 20 , 10 , e 1

print('=== Caixa AquiTem ===')
print('Cédulas disponíveis: R$50, R$20, R$10 e R$1')
valor = int(input('Valor do saque: '))
valorTotal = valor
ced = 50
totalCedula = 0

while True:
  if valorTotal >= ced:
    valorTotal -= ced
    totalCedula += 1
  else:
  # if totalCedula > 0:
    print(f'Total de {totalCedula} cédula(s) de R${ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totalCedula = 0
    if valorTotal == 0:
      break
