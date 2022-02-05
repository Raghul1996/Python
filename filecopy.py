f=open("a.txt",'r')
d="instead"
flag=0
index=0
filereader=open("b.txt",'w')
for f1 in f:
    index+=1
    if d in f1:
        flag=1
        break
if flag==1:
        print('String',d,'found in file at',index,'th line')
else:
    print('string',d,'not found in file')
    #else:
        #print('String',d,'Not found')
    #filereader.write(f1)



