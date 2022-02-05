def calculateGrade(students_marks):
    li_new=[]
    sum_val=0
    #print(students_marks)
    li_len=len(students_marks)
    #print(li_len)
    for i in students_marks:
        #print(type(i))
        #print(type(students_marks))
        sum_val+=i
    res=sum_val/li_len
    print(res)
    if(res >= 90):
        grade='A'
    elif(res >=80 and res<=90):
        grade="A"
    elif(res >=70 and res<=80):
         grade="B"
    elif(res >=60 and res<=70):
         grade="C"
    elif(res >=50 and res<=60):
         grade="D"
    else:
        grade="F"
    return grade  

grade_val=calculateGrade([66,61,88,26,13])
print(grade_val)