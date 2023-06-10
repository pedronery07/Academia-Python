def nota_final(medq, AI, AF, EP1, EP2, PF):
    if medq < 0 or AI < 0 or AF < 0 or EP1 < 0 or EP2 < 0 or PF < 0:
        return 0
    elif medq > 10 or AI > 10 or AF > 10 or EP1 > 10 or EP2 > 10 or PF > 10:
        return 0
    ni = 0.4*AI + 0.5*AF + 0.1*medq
    ng = 0.1*EP1 + 0.2*EP2 + 0.7*PF
    if ni >= 5 and ng >= 5:
        nf = (ni + ng)/2
    else:
        nf = min(ni, ng)
    return nf