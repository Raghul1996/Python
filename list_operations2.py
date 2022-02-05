def tuplefunction(list1, list2, string1, n):
    tuple1=tuple(list1)
    tuple2=tuple(list2)
    print(tuple1+tuple2)
    tuple3=tuple1+tuple2
    print(tuple3[4])
    res=(tuple1,tuple2)
    print(res)
    print(len(res))
    new_tupl2=(string1,)*n
    print(new_tupl2)
    print(max(tuple1))
tuplefunction([1,2,6],['text1','text2','text3'],'word',3)