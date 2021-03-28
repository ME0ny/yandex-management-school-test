import csv

month = [
    {
        'id':[],
        'revenue': [0 for i in range(12)]
    },
]

with open('purchases.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=' ')
        

print(month)
