n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
Soma = n1 + n2
Multiply = n1 * n2
Divisao = n1 / n2
DivisaoInteira = n1 // n2
Exponenciacao = n1 ** n2
print('A soma dos valores vale: {}, o produto é {} e a divisão: {:.3f}.' .format(Soma, Multiply, Divisao), end=' ')
print('A divisão inteira vale {} e a potência é {}' .format(DivisaoInteira, Exponenciacao))
# Para quebrar a linha: \n