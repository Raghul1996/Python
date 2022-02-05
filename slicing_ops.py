def sliceit(mylist):
    print(mylist[1:3])
    print(mylist[1::2])
    newlist=mylist[::-1]
    print(newlist[:3])

sliceit([3,4,3,2,6,1,2,6])