def calculateNTetrahedralNumber(startvalue, endvalue):
    tetrahead=[]
    while startvalue <= endvalue:
        tetrahead_val=int(((startvalue)*(startvalue+1)*(startvalue+2))/6)
        tetrahead.append(tetrahead_val)
        startvalue+=1
    return tetrahead

t_val=calculateNTetrahedralNumber(1,7)
print(*t_val,sep="\n")
