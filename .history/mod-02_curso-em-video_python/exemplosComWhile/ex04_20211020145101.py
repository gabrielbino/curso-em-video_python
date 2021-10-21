# ler o nome e o preço de vários produtos perguntando se quer continuar
# no final. mostrar o total gasto. Quantos produtos custam mais de 100 e
# o nome do produto mais barato.

maiorQ = maisBarato = 0
resp = 'S'
print('=== DevBino Store ===')

while resp in 'S':
  nomeProduto = str(input('Nome do produto: '))
  precoProduto = int(input('Preço do produto: '))
  if precoProduto > 100:
    maiorQ += 1

  while resp not in 'N':
    resp = str(input('Quer continuar? [S/N]: ')).upper().split()[0]
    if resp == 'N':
      break


print(f'{maiorQ} produto(s) custa(m) mais que R$ 100,00.')
# print(f'O produto mais barato custa R$ {maisBarato}')
