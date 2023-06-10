d = int(input('Quantidade de dias: '))
h = int(input('Quantidade de horas: '))
m = int(input('Quantidade de minutos: '))
s = int(input('Quantidade de segundos: '))

s1 = m*60
s2 = h*3600
s3 = d*86400

print(s1+s2+s3+s)