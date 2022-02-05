import csv

with open("ngm.csv",'r') as filenew:
    csvread=csv.reader(filenew)
    head=next(csvread)
    print(head)
    for r in csvread:
        head.append(r)
print(head)