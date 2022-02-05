import math
def circle(c):
    pi_val=math.pi
    rad=c/(2*pi_val)
    rad_val=round(rad,2)
    area=pi_val*rad*rad
    area_val=round(area,2)
    return((rad_val,area_val))
print(circle(8))

