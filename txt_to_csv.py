import pandas as pobj

def convert_csv_to_txt():
    csvread=pobj.read_csv('txt_to_csv.txt')
    csvread.to_csv('txt_to_csv.csv')

convert_csv_to_txt()

