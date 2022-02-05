def duplication_removal_list(values_li:list)->None:
    values_li=list(dict.fromkeys(values_li))
    print(values_li)
    print(type(values_li))

duplication_removal_list([1,2,2,3,4,5,6,7,6,5])