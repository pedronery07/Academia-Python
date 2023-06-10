classif = str(input('Classificação? '))
v = int(input('Quantos vermelhos estão aguardando? '))
l = int(input('Quantos laranjas estão aguardando? '))
a = int(input('Quantos azuis estão aguardando? '))

if classif == 'V':
    print(7*v)
elif classif == 'L':
    print(7*v + 5*l)
elif classif == 'A':
    print(7*v + 5*l + 5*a)