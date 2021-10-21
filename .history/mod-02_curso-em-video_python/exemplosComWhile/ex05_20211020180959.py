# simular um caixa eletrônico. perguntar qual valor será sacado (int)
# Informar quantas cédulas serão entregues.
# Considere que o caixa tem: 50 , 20 , 10 , e 1

print('=== Caixa AquiTem ===')
print('Cédulas disponíveis: R$50, R$20, R$10 e R$1')
valor = int(input('Valor do saque: '))
total = valor
ced = 50
totced = 0

while True:
  if total >= ced:
    total -= ced
    totced += 1
  else:
  # if totced > 0:
    print(f'Total de {totced} cédula(s) de R${ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totced = 0
    if total == 0:
      break
