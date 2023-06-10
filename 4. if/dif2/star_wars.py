pontos = 0
q1 = str(input('Já assistiu todos os filmes?'))
if q1 == 'sim':
    pontos += 1
q2 = str(input("Tem camiseta temática?"))
if q2 == 'sim':
    pontos += 1 
q3 = str(input("Já se fantasiou de algum personagem?"))
if q3 == 'sim':
    pontos += 1
q4 = str(input("Tem algum action figure/nave/etc?"))
if q4 == 'sim':
    pontos += 1
q5 = str(input("Já foi no Galaxy's Edge, o parque temático da franquia?"))
if q5 == 'sim':
    pontos += 1

if pontos < 2:
    print('Inocente')
if pontos == 2:
    print('Padawan')
elif pontos == 3 or pontos == 4:
    print('Jedi')
elif pontos == 5:
    print('One with the Force')