def myDict(key1, value1, key2, value2, value3, key3):
    dict1={key1:value1}
    print(dict1)
    dict1[key2]=value2
    print(dict1)
    dict1[key1]=value3
    print(dict1)
    del dict1[key3]
    return dict1

newdict=myDict('name','rajesh','age','21','vignesh','age')
print(newdict)