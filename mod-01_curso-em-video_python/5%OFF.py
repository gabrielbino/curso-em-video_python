# Ler o preço de um produto e mostrar seu preço com 5% de desconto

""" precoProduto = float(input('Qual o valor do produto? '))
desconto = float(.05 * precoProduto)
precoComDesconto = float(precoProduto - desconto)
print('O produto com (5%) de desconto vale: R$ {:.2f}' .format(precoComDesconto)) """

# Forma simplificada
precoProduto = float(input('Qual o valor do produto? '))
precoComDesconto = precoProduto - (.05 * precoProduto)
print(f'O produto com (5%) de desconto vale: R$ {precoComDesconto:.2f}')

