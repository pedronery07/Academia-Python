from math import pi
def will_it_float(p, r, rst):
    r_m = r*(10**-2) 
    rst_m = rst*(10**-2)
    v = 2*(pi**2)*r_m*(rst_m**2)
    densidade = p/v
    if densidade <= 997:
        return True
    else:
        return False