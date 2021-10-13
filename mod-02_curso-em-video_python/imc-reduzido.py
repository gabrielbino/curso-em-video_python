# IMC. Ler o peso e a altura do usuário e mostrar:
# <= 18.5: abaixo do peso | entre 18.5 e 25: peso ideal | 25 a 30: sobrepeso
# 30 a 40: obesidade | >40: obesidade mórbida

peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))

imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.2f}! ', end='')

if imc < 18.5:
  print('Você está abaixo do seu peso ideal.')
elif 18.5 <= imc < 25:
  print('Você está no seu peso ideal.')
elif 25 >= imc < 30:
  print('Você está na faixa de sobrepeso.')
elif 30 >= imc < 40:
  print('Você está na faixa de obesidade.')
else:
  print('Você está na faixa de obesidade mórbida.')