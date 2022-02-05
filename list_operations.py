def List_Op(Mylist, Mylist2):
    print(Mylist)
    print(Mylist[1])
    print(Mylist[-1])
    Mylist.append(3)
    Mylist[3]=60
    print(Mylist)
    print(Mylist[1:5])
    Mylist.append(Mylist2)
    print(Mylist)
    Mylist.extend(Mylist2)
    print(Mylist)
    del Mylist[-1]
    print(Mylist)
    print(len(Mylist))


lst1=[1,2,3,4,5]
lst2=[6,7,8]
List_Op(lst1,lst2)