import pandas as p
#obj=p.read_csv('ngm.csv',header=None)
#obj=p.read_csv('ngm.csv',usecols=['Reference Id'])
obj=p.read_csv('ngm.csv',usecols=['Emp Id'])
ob=p.DataFrame(obj)
print(ob.sum())