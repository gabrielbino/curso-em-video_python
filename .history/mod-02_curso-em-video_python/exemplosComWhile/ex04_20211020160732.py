# ler o nome e o preço de vários produtos perguntando se quer continuar
# no final. mostrar o total gasto. Quantos produtos custam mais de 100 e
# o nome do produto mais barato.

print('=== DevBino Store ===')
total = 0
while True:
  produto = str(input('Nome do produto: '))
  preco = float(input('Preço: R$ '))
  total += preco
  
  resp = ' '
  resp = str(input('Quer continuar? [S/N]: ')).upper().split()[0]
  if resp == 'N':
    break
