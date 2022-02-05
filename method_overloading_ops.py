from typing import overload
from multipledispatch import dispatch

class OVERLOAD:
    def __init__(self,a):
            self.a=a
    
    @dispatch(int,int,int)
    def add(first,second,third):
        result=first*second*third
        print(result) 
    
    @dispatch(int,int)
    def add(first,second):
        result=first*second
        print(result) 

    @dispatch(float,float)
    def add(first,second):
        result=first*second
        print(result) 

ov=OVERLOAD(1)
ov.add(1,2)
ov.add(2,2,2)
ov.add(2.3,2.3)
