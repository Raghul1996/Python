import math
def triangle(n1, n2, n3):
    area=(n1*n2)/2
    round_area=round(area,n3)
    round_pi=round(math.pi,n3)
    return(round_area,round_pi)


a=triangle(9,5,4)
print(a)