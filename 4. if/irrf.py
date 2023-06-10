sb = float(input('Salário bruto: '))
dep = float(input('Dependentes: '))

if sb < 1045:
    inss = sb*0.075
elif 1045.01 < sb <= 2089.60:
    inss = sb*0.09
elif 2089.60 < sb <= 3134.40:
    inss = sb*0.12
elif 3134.40 < sb <= 6101.06:
    inss = sb*0.14
else:
    inss = 671.12

base = sb - inss - dep * 189.59

if base <= 1903.98:
    al = 0
    deducao = 0
elif 1903.99 < base <= 2826.65:
    al = 0.075
    deducao = 142.80
elif 2826.66 < base <= 3751.05:
    al = 0.15
    deducao = 354.80
elif 3751.05 < base <= 4664.68:
    al = 0.225
    deducao = 636.13
else:
    al = 0.275
    deducao = 869.36

IRRF = base*al - deducao
print(IRRF)