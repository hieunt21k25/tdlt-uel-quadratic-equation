import math


def first_degree(a,b):
    if a == 0:
        if b == 0:
            return "INF"
        else:
            return "No Solution"
    else:
        x = -b / a
        return "x={}".format(x)
def quadratic(a,b,c):
    if a==0:
        return first_degree(b,c)
    elif a==0 and b==0:
        return "No solution"
    elif a==0 and b==0 and c==0:
        return "Inf Solution"
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "VN"
        elif delta == 0:
            return "x1=x2={}".format(-b / (2 * a))
        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
        return "x1={}, x2={}".format(x1, x2)