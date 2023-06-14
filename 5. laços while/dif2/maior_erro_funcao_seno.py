from math import sin, radians

i = 0
maior = 0
dif = 0

while i <= 90:
    bhask = ((4*i*(180-i))/(40500-i*(180-i)))
    math = (sin(radians(i)))
    if abs(math - bhask) > dif:
        dif = abs(math - bhask)
        maior = i
    
    i += 1

print(maior)