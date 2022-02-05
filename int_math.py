from distutils.command.sdist import sdist


import math
def Integer_math(Side,Radius):
    area_s=Side*Side
    volume_c=Side*Side*Side
    area=math.pi*Radius*Radius
    volume=(4*math.pi*Radius*Radius*Radius)/3
    print(f'Area of Square is',round(area_s))
    print(f'Volume of Cube is',round(volume_c))
    print(f'Area of Circle is',round(area,2))
    print(f'Volume of Sphere is',round(volume,2))
    
Integer_math(5,7)