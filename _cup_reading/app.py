from time import time, ctime, sleep
import os

import pandas as pd



"""
I need to read excel file to Pandas DataFrame
Make dict of this data
Append this dicts to list
Save this list to file for some time interval, ex 1M or 10M or so on...
OR
Add it to DataBase!!!
Excel file should save every second
"""

# def f():
#     print('This is your one second interval')

# start_time = time.time()
# interval = 1
# for i in range(20):
#     time.sleep(start_time + i*interval - time.time())
#     f()

#
LIST_ALL_EXCEL_SHEET: list = []


def read_excel():
    excel_cup = pd.read_excel('ri_cup.xlsx', sheet_name='Sheet1',)
                    # header=0, names=['purchase', 'purchase_price','sale_price', 'sale'],)
                    # converters={"purchase": int, "purchase_price": int, "sale_price": int, "sale": int})
    excel_cup.columns = ['purchase','purchase_price','sale_price','sale']
    return excel_cup


def df_to_list(read_excel):
    for index, rows in read_excel.iterrows():
        # print(index, rows)
        my_list: list = [rows.purchase, rows.purchase_price,
                        rows.sale_price, rows.sale,]
        LIST_ALL_EXCEL_SHEET.append(my_list)



# Save to file deals.py
def save_deals(deals_list=LIST_ALL_EXCEL_SHEET):
    with open('cup.py', 'w') as f:
        f.write(str(LIST_ALL_EXCEL_SHEET))
        # print('Data rewritred and saved to cup.py')

# df_to_list(read_excel())

# for el in LIST_ALL_EXCEL_SHEET:
#     t = time()
#     el.append(ctime(t))
# save_deals()
# print(time.time(1635417727.911163))


start_time = time()
interval = 1
for i in range(20):
    sleep(start_time + i*interval - time())
    df_to_list(read_excel())
    # for el in LIST_ALL_EXCEL_SHEET:
    #     t = time()
    #     el.append(ctime(t))
    save_deals()
print('Done')