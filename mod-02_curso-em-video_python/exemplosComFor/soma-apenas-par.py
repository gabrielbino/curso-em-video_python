# Ler 6 números inteiros e somar apenas os números pares
# desconsiderar os ímpares

acumulador = 0
for c in range(0, 6):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    acumulador += n
print(f'A soma dos valores pares exibidos foi: {acumulador}')