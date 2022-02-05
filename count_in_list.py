from collections import Counter

def count_items_in_list(numbers_list:list)->None:
    count_items=Counter(numbers_list)
    print(count_items)
    print(type(count_items))

count_items_in_list([1,2,1,2,4,3,4,5,6,7,8])
