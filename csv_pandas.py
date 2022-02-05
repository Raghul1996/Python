import pandas as pd

#p=pd.read_csv('ngm.csv',skiprows=1)
p=pd.read_csv('ngm.csv')
print(p.head(5))
print(p['Pincode'].dtypes)