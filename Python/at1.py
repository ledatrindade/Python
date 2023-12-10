import math

raio = float(input('Digite o raio da circunferência: '))

diametro = 2 * raio
area = math.pi * raio **  2
perimetro = diametro * math.pi 

print(f'Diâmetro da circunferência:%.2f' % diametro)
print(f'Área da circunferência:%.2f' % area)
print(f'Perímetro da circunferência:%.2f' % perimetro)