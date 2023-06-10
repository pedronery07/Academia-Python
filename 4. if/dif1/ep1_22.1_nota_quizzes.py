def nota_quizzes(q1, q2, q3, q4, q5):
    l = [q1, q2, q3, q4, q5]
    if q1 > 10 or q1 < 0:
        return 0
    if q2 > 10 or q2 < 0:
        return 0
    if q3 > 10 or q3 < 0:
        return 0
    if q4 > 10 or q4 < 0:
        return 0
    if q5 > 10 or q5 < 0:
        return 0
    descarte = min(l)
    media = (sum(l) - descarte)/4
    return media