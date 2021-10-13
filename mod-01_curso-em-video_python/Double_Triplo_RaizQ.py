# Ler um número inteiro
# Exibir o seu dobro, o triplo e a raiz quadrada

# numInt = int(input('Digite um número inteiro: '))
# double = (numInt * 2)
# triplo = (numInt * 3)
# raizQ = (numInt ** (1/2))
# print('O dobro de {} é: {}' .format(numInt, double))
# print('O triplo de {} é: {}. \nA raiz quadrada de {} é: {:.2f}' .format(numInt, triplo, numInt, raizQ))

# Forma simplificada
numInt = int(input('Digite um número inteiro: '))
print('O dobro de {} é: {}' .format(numInt, (numInt * 2)))
print('O triplo de {} é: {}. \nA raiz quadrada de {} é: {:.2f}' .format(numInt, (numInt * 3), numInt, (numInt ** (1/2))))
 # pow(numInt, (1/2)) <- Também calcula a raizQ de numInt