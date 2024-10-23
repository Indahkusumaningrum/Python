
def hitung_diskon(row):
    total_diskon = row['Fee'] * row['Percentage Discount'] * 0.01
    return total_diskon

def hitung_total(row):
    total_diskon = hitung_diskon(row)

    if row['Categories'] == 'PI':
        total = row['Fee'] * row['Duration'] - total_diskon
    else:
        total = row['Fee'] * row['Duration'] - total_diskon - (total_diskon * 0.02)

    return total