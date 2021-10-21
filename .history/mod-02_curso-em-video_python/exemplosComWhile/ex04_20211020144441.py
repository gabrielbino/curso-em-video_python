# ler o nome e o preço de vários produtos perguntando se quer continuar
# no final. mostrar o total gasto. Quantos produtos custam mais de 100 e
# o nome do produto mais barato.

maiorQ = produtoMaisBarato = 0
resp = ' '
print('=== DevBino Store ===')

while resp not in 'N':
  nomeProduto = str(input('Nome do produto: '))
  precoProduto = int(input('Preço do produto: '))
  if precoProduto > 100:
    maiorQ += 1

  resp = str(input('Quer continuar? [S/N]: ')).upper().split()[0]


print(f'{maiorQ} produto(s) custa(m) mais que R$ 100,00.')
# print(f'O produto mais barato custa R$ {produtoMaisBarato}')
