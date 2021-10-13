# for contador in range(5, 0, -1):
#   print(contador)
# print('Fim!')

# for contador in range(1, 6, 2):
#   print(contador)

# inicio = int(input('Início: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))
# for c in range(inicio, fim+1, passo):
#   print(c)

somatorio = 0
for c in range(0, 3):
  n = int(input('Digite um valor: '))
  somatorio += n # somatorio = somatorio + n
print(f'O somatório dos números deu {somatorio}')