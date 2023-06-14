l = []
while True:
    num = int(input('Digite um número: '))
    if num <= 0:
        break
    l.append(num)
l.sort(reverse=True)
print(l)