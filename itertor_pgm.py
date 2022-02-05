li=[1,2,3,4,5]

itr=iter(li)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break