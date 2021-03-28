import csv

struct = {
        'id':[],
        'id_day': {},
        'revenue': [0 for i in range(7)],
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
        'id_day': {},
        'revenue': [0 for i in range(13)],
        'count': [0 for i in range(13)],
        'len': 0,
})
            print(month[n - 1])

        for i in range(n):
            #print(month[i][0])
            if (curr_id in month[i]['id']):
                flag = True
                month[i]['revenue'][n - 1] += curr_revenue
                month[i]['count'][n - 1] += 1
                month[i]['id_day'][curr_id] = n - i
        if (flag == False):
            month[n - 1]['id'].append(curr_id)
            month[n - 1]['revenue'][n - 1] += curr_revenue
            month[n - 1]['len'] += 1
            month[i]['count'][n - 1] += 1
            month[i]['id_day'][curr_id] = 1
        flag = False
        last_month = curr_month
for i in range(12):
    main_summ = 0
    ap = 0
    all_sale = 0
    av_count_sale = 0
    print("month:", i, " len:", month[i]['len'])
    for j in range(12):
        main_summ += float('{:.3f}'.format(month[i]['revenue'][j]))
        all_sale += month[i]['count'][j]
        print(j, "\t", float('{:.3f}'.format(month[i]['revenue'][j])), "\t", 
        float('{:.3f}'.format(month[i]['revenue'][j] / month[i]['len'])), "\t", 
        month[i]['count'][j], "\t", end = '')
        try:
            print(float('{:.3f}'.format(month[i]['revenue'][j])) / month[i]['count'][j])
        except:
            print(0)
    print("summ:", main_summ)
    lt = [0 for j in range(13)]
    for j in month[i]['id']:
        lt[month[i]['id_day'][j]] += 1
    lt_res = 0
    day = 0
    for j in lt:
        lt_res += (int(j) /  month[i]['len']) * day
        day += 1 
    ap = main_summ / all_sale
    av_count_sale = all_sale / month[i]['len']
    print("LT:", lt_res)
    print("AP:", ap)
    print("ACS:", av_count_sale)
    print("LTV:", lt_res * ap * av_count_sale)
    print()