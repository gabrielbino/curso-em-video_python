# Ler o sexo de uma pessoa, mas só aceitar 'M' ou 'F'
# caso contrário, pedir pra digitar novamente!

sexo = str(input('Informe seu sexo: ')).strip()[0] # Pega só a primeira letra
while sexo not in 'MmFf': # Enquanto sexo não estiver em 'MmFf'
  sexo = str(input('Dados inválidos, informe seu sexo [M/F]: ')).upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')