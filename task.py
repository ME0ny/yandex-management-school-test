import csv

struct = {
        'id':[],
        'revenue': [0 for i in range(21)],
        'len': 0,
}
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
        curr_revenue = float(row["revenue"])
        if last_month != curr_month:
            print(n)
            n+=1
            month.append({
        'id':[],
        'revenue': [0 for i in range(21)],
        'len': 0,
})
            print(month[n - 1])

        for i in range(n):
            #print(month[i][0])
            if (curr_id in month[i]['id']):
                flag = True
                month[i]['revenue'][n - 1] += curr_revenue
        if (flag == False):
            month[n - 1]['id'].append(curr_id)
            month[n - 1]['revenue'][n - 1] += curr_revenue
            month[n - 1]['len'] += 1
        flag = False
        last_month = curr_month
        if (n == 12):
            break
for i in range(5):
    print("month:", i, " len:", month[i]['len'])
    for j in range(21):
        print(j, float('{:.3f}'.format(month[i]['revenue'][j])), float('{:.3f}'.format(month[i]['revenue'][j] / month[i]['len'])))
    print()
