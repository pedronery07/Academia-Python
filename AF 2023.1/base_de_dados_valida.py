def base_de_dados_valida(lista_livros):
    # Cria lista que conterá todos os ISBNs de cad livro
    isbn_lista = []
    # Percorre livros para adicioná-los na lista criada e verifica se há ISBNs repetidos na lista
    for livro in lista_livros:
        if livro[1] not in isbn_lista:
            isbn_lista.append(livro[1])
        else:
            return False
    return True