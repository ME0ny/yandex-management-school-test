import csv

struct = {
        'id':[],
        'revenue': [0 for i in range(12)],
        'len': 0
    },
month = []
last_month = ""
curr_month = ""
flag = False
with open('purchases.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=' ')
    n = 0
    for row in reader:
        curr_month = row["buy_ts"][3:]
        curr_id = row["uid"]
        curr_revenue = row["revenue"]
        if last_month != curr_month:
            n+=1
            month.append(struct)
        for i in range(n):
            if (curr_id in i['id']):
                flag = True
                month[i]['revenue'][n - 1] += curr_revenue
        if (flag == False):
            month[n - 1]['id'].append(curr_id)
            month[n - 1]['revenue'][n - 1] += curr_revenue
            month[n - 1]['len'] += 1
        flag = False
        last_month = curr_month
                
      

print(month)
