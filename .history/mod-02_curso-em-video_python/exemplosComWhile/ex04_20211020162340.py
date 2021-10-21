# ler o nome e o preço de vários produtos perguntando se quer continuar
# no final. mostrar o total gasto. Quantos produtos custam mais de 1000 e
# o nome do produto mais barato.

total = maiorMil = menorPreco = cont = 0
print('=== DevBino Store ===')
while True:
  produto = str(input('Nome do produto: '))
  preco = float(input('Preço: R$'))
  total += preco
  cont += 1
  
  if preco > 1000:
    maiorMil += 1

  if cont == 1:
    menorPreco = preco
    nomeMenorPreco = produto
  else:
    if preco < menorPreco:
      menorPreco = preco
      nomeMenorPreco = produto

  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N]: ')).upper().split()[0]
  if resp == 'N':
    break

print(f'Total gasto: R${total:.2f}')
print(f'Produtos acima de R$ 1.000,00: {maiorMil}')
print(f'O produto mais barato é o {nomeMenorPreco}. Custa R${menorPreco:.2f}')
