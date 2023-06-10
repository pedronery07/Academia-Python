from math import e

taxa = float(input("Qual a taxa (λ)? "))
x = float(input("Qual x, para calcular F(λ, x)?"))

f = 1 - e**(-taxa*x)

print('{0:.4f}'.format(f))