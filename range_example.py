def gen(startval,endval):
    #x=range(startval,startval+3)
    x=slice[startval,startval+3]
    for n in x:
        print(n)
    x1=range(endval,endval-5)
    for n1 in x1:
        print(n1)
gen(10,15)