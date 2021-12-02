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
Excel file is saving onChange
"""

# def f():
#     print('This is your one second interval')

# start_time = time.time()
# interval = 1
# for i in range(20):
#     time.sleep(start_time + i*interval - time.time())
#     f()

#
# LIST_ALL_EXCEL_SHEET: list = []


def read_excel():
    excel_cup = pd.read_excel('ri_cup.xlsm', sheet_name='Sheet1',)
                    # header=0, names=['purchase', 'purchase_price','sale_price', 'sale'],)
                    # converters={"purchase": int, "purchase_price": int, "sale_price": int, "sale": int})
    excel_cup.columns = ['purchase','purchase_price','sale_price','sale']
    return excel_cup


def df_to_list(read_excel):
    list_all_excel_sheet: list = []
    for index, rows in read_excel.iterrows():
        # print(index, rows)
        my_list: list = [rows.purchase, rows.purchase_price,
                        rows.sale_price, rows.sale,]
        list_all_excel_sheet.append(my_list)
    
    return list_all_excel_sheet




# Save to file deals.py
# def save_deals(deals_list=LIST_ALL_EXCEL_SHEET):
def save_deals(result):
    with open('cup.py', 'a') as f:
        f.write(str(result))
        # print('Data rewritred and saved to cup.py')


# for el in LIST_ALL_EXCEL_SHEET:
#     t = time()
#     el.append(ctime(t))
# save_deals()
# print(time.time(1635417727.911163))



start_time = time()
interval = 5
for i in range(4):
    sleep(start_time + i*interval - time())
    save_deals(df_to_list(read_excel()))

    # for el in LIST_ALL_EXCEL_SHEET:
    #     t = time()
    #     el.append(ctime(t))


print('Done')
