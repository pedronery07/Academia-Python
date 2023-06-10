def valida_cpf(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11):
    if n1 == n2 == n3 == n4 == n5 == n6 == n7 == n8 == n9 == n10 == n11:
        return False
    verif1 = 10*n1 + 9*n2 + 8*n3 + 7*n4 + 6*n5 + 5*n6 + 4*n7 + 3*n8 + 2*n9
    if (verif1*10) % 11 == n10 or (verif1*10) % 11 == 10 and n10 == 0:
        verif2 = 11*n1 + 10*n2 + 9*n3 + 8*n4 + 7*n5 + 6*n6 + 5*n7 + 4*n8 + 3*n9 + 2*n10
        if (verif2*10) % 11 == n11 or (verif1*10) % 11 == 10 and n11 == 0:
            return True
        else:
            return False
    else:
        return False