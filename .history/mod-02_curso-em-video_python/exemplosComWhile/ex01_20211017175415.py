n = cont = soma = 0
while n != 999:
  n = int(input('Digite um número [999 para sair]: '))
  if n == 999:
    break
  cont += 1
  soma += n
print(f'A quantidade de números digitados foi {cont} e a soma entre eles foi {soma}.') 
