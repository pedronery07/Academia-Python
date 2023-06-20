l1 = []
while True:
    u = str(input(' '))
    if u == 'fim':
        break
    l1.append(u)

l2 = []
for i in range(len(l1)):
    if l1[i] not in l2:
        print(f'{l1[i]}')
    else:
        cont = l2.count(l1[i])
        cont_str = str(cont)
        string_corr = l1[i] + cont_str
        print(f'{string_corr}')
    l2.append(l1[i]) 