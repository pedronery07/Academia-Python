#Usando dicionario
#mes = str(input("Qual é o nome do mês?"))

#dicionario = {"janeiro":1 , "fevereiro":2 , "março":3, "abril":4, "maio":5, "junho":6, "julho":7, "agosto":8, "setembro":9, "outubro":10, "novembro":11, "dezembro":12}

#print(dicionario[mes])

#Usando lista
mes = str(input("Qual é o nome do mês?"))

l = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

for i in range(len(l)):
    if l[i] == mes:
        print(i+1)