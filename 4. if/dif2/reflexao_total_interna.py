from math import radians, sin
def reflexao_total_interna(n1, n2, theta2):
    st1 = n1/n2
    rt2 = radians(theta2)
    if sin(rt2) > st1:
        return True
    else:
        return False