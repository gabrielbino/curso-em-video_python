# Ler o peso de 5 pessoas e mostrar o maior e menor peso.

maiorPeso = 0
menorPeso = 0
for c in range(1, 6):
  peso = int(input(f'Peso da {c}º pessoa (Kg): '))
  if c == 1:
    maiorPeso = peso
    menorPeso = peso
  else:
    if peso > maiorPeso:
      maiorPeso = peso
    if peso < menorPeso:
      menorPeso = peso
print(f'O maior peso é {maiorPeso} Kg.')
print(f'O menor peso é {menorPeso} Kg.')