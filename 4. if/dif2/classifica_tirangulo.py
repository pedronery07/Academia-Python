def classifica_triangulo(l1, l2, l3):
    if l1 == l2 and l2 == l3:
        return 'equilátero'
    elif l1 == l2 and l2 != l3:
        return 'isósceles'
    elif l2 == l3 and l1 != l2:
        return 'isósceles'
    elif l1 == l3 and l1 != l2:
        return 'isósceles'
    elif l1 != l2 and l2 != l3:
        return 'escaleno'