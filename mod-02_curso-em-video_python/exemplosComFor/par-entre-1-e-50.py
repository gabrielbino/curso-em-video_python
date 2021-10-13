# Mostrar todos os nº pares que estão entre 1 e 50

for c in range(1, 50):
  if c % 2 == 0:
    print(c)
# Essa lógica faz com que o laço rode mais do que o necessário

# Exemplo:
for c in range(1, 50):
  print('.', end='')
  if c % 2 == 0:
    print(c, end=' ')

# Para reduzir essas voltas desnecessárias:
for c in range(2, 51, 2):
  print('.', end='')
  print(c, end=' ')