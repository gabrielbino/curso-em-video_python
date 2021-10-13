# Calcular a soma de todos os nº ímpares que são múltiplos de 3
# e que se encontram no intervalo entre 1 e 500

contador = 0
acumulador = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    contador += 1
    acumulador += c
print(f'A soma de todos os {contador} valores múltiplos de 3 é: {acumulador}')