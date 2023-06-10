from math import sin, radians
v = float(input('Velocidade: '))
a = float(input('Ângulo de lançamento: '))
g = 9.8

a_rad = radians(a)

d = (v**2*(sin(2*a_rad)))/g
if d >= 98 and d <= 102:
    print('Acertou!')
elif d < 98:
    print('Muito perto')
else:
    print('Muito longe')  