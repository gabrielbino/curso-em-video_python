# Ler 3 valores e dizer se dá pra formar um triângulo.
# Dizer se é o triângulo é equilátero (todos os lados iguais),
# Isósceles (dois lados iguais) ou escaleno (todos os lados diferentes)

valor1 = float(input('Informe o primeiro segmento: '))
valor2 = float(input('Informe o segundo segmento: '))
valor3 = float(input('Informe o terceiro segmento: '))

if (
  valor1 < valor2 + valor3 and
  valor2 < valor1 + valor3 and
  valor3 < valor1 + valor2):
  print('Os segmentos acima podem formar um triângulo', end=' ')
  if valor1 == valor2 == valor3:
    print('EQUILÁTERO!')
  elif valor1 != valor2 != valor3 != valor1:
    print('ESCALENO!')
  else:
    print('ISÓSCELES!') 
else:
  print('Os segmentos acima NÃO podem formar um triângulo!')