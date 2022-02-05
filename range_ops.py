def generateList(startvalue, endvalue):
    li=[]
    for i in range(startvalue,endvalue+1):
        li.append(i)
    #len_li=len(li)
    print(li[:3])
    myli=li[::-1]
    print(myli[:5])
    #print(li)
    #li.reverse()
    #print(li)
    print(li[::4])
    print(myli[::2])

generateList(10,16)