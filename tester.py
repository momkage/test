import csv

with open('jan.csv' , 'r') as f:
    csvreader = csv.reader(f)
    print(csvreader)