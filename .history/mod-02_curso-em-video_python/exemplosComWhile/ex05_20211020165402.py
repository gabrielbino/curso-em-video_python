# simular um caixa eletrônico. perguntar qual valor será sacado (int)
# Informar quantas cédulas serão entregues.
# Considere que o caixa tem: 50 , 20 , 10 , e 1

print('=== Caixa AquiTem ===')
print('Cédulas disponíveis: R$50, R$20, R$10 e R$1')
valor = int(input('Valor do saque: '))
total = valor

maiorCedula = 50
totalCedula = 0

while True:
  if total >= maiorCedula:
    total -= maiorCedula
    totalCedula += 1
  else:
    if totalCedula > 0:
      print(f'Total de {totalCedula} cédula(s) de R${maiorCedula}')
    if maiorCedula == 50:
      maiorCedula = 20
    elif maiorCedula == 20:
      maiorCedula = 10
    elif maiorCedula == 10:
      maiorCedula = 1
    totalCedula = 0
    if totalCedula == 0:
      break
