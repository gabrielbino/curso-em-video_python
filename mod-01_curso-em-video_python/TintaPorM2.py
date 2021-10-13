# Ler a altura e largura de uma parede em metros
# Calcular a área e a quantidade de tinta necessária para pintá-la
# Sabendo que cada Litro de tinta pinta uma área de 2m^2

# b * h = A

b = float(input('Digite a largura do ambiente (em metros): '))
h = float(input('Digite a altura do ambiente (em metros): '))
A = float(b * h)
tinta = float(A / 2)
print('Será(ão) necessário(os) {}L de tinta para pintar {}m^2 do ambiente!' .format(tinta, A))
