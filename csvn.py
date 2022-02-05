import csv

filenew=open("business-operations-survey-2020-covid-19.csv")
csv_reader=csv.reader(filenew)
snew=[]
snew=next(csv_reader)
print(snew)
for f in csv_reader:
    snew.append(f)
print(f)
filenew.close()
