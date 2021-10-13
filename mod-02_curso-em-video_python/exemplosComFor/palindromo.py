# Ler uma frase qualquer e dizer se ela é palíindromo
# desconsiderando os espaços.
# Exemplo: APOS A SOPA (a leitura é igual de trás pra frente)

frase = str(input('Digite uma frase: ')).strip().upper() # Tirei os espaços antes e depois e coloquei tudo em maiúsculo
dividirPavaras = frase.split() # Separei palavra por palavra em uma lista.
juntarPavaras = ''.join(dividirPavaras) # Juntei tudo em uma única string, sem espaço.
inverso = juntarPavaras[::-1] # Técnina de fatiamento | Começa do início, não pega nada, termina no fim e volta de trás pra frente.
# inverso = ''
# for letra in range(len(juntarPavaras) - 1, -1, -1):
#   inverso += juntarPavaras[letra]
print(f'O inverso de {juntarPavaras} é {inverso}.')

if inverso == juntarPavaras:
  print('Temos um palíindromo!')
else:
  print('NÃO temos um palíindromo!')