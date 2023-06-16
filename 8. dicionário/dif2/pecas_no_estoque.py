def tem_estoque(pecas, estoque):
    for parte, qtde in pecas.items():
        if parte not in estoque.keys():
            return False
        else:
            if estoque[parte] < qtde:
                return False
            else:
                estoque[parte] -= qtde
    return True