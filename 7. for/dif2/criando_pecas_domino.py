from random import shuffle
def cria_pecas():
    pecas = []
	# Cria numeração da equerda
    for i in range(7):
        j = i
		# Cria numeração da direita e completa a peça
        for e in range(j,7):
            p = [i,e]
            pecas.append(p)

    shuffle(pecas)
    return pecas