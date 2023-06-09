from math import degrees, radians, asin, sin

def snell_descartes(n1,n2,t1):
    rt1 = radians(t1)
    srt2 =  n1 * sin(rt1) / n2
    rt2 = asin(srt2)
    t2 = degrees(rt2)
    return t2