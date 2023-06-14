A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
total = 0

while True:
    i = int(input('Idade do paciente: '))
    if i < 0:
        break
    if i >= 0 and i <= 11:
        A += 1
    elif i >= 12 and i <= 17:
        B += 1
    elif i >= 18 and i <= 25:
        C += 1
    elif i >= 26 and i <= 35:
        D += 1
    elif i >= 36 and i <= 59:
        E += 1
    else:
        F += 1 
    total += 1

print(f'0-11 anos: {A/total*(100):.2f} %')
print(f'12-17 anos: {B/total*(100):.2f} %')
print(f'18-25 anos: {C/total*(100):.2f} %') 
print(f'26-35 anos: {D/total*(100):.2f} %') 
print(f'36-59 anos: {E/total*(100):.2f} %')
print(f'Acima de 60 anos: {F/total*(100):.2f} %')