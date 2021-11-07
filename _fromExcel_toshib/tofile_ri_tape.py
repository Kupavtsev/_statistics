import pandas as pd
import os
import time
import sys

# Path to file
try:
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "D:/Dropbox/TRADING/_deals_for_python/ri_201021.xlsx"
    abs_file_path = os.path.join(script_dir, rel_path)
except:
    print('I cand find Excel file')

# reading excel file
EXCEL_SHEET = pd.read_excel(abs_file_path, sheet_name='Лист1',
                        names=['count_num', 'num', 'date', 'ses_date','time', 'instrument',
                        'price', 'quantity', 'volume', 'transaction'],
                        converters={"time": str,
                        "price": str})


# Global vars
LIST_ALL_EXCEL_SHEET: list = []
RESULTED_LIST_EN: list = []
RESULTED_LIST_PRICE: list = []

# list all deals from Data Frame
def df_to_list(excel_sheet=EXCEL_SHEET):
    for index, rows in excel_sheet.iterrows():
        # print(index, rows)
        # rows.num
        my_list: list = [rows.count_num, rows.date,
                        rows.ses_date, rows.time,
                        rows.instrument, rows.price,
                        rows.quantity, rows.transaction]
        b = ("Loading: " + str(my_list[0]))
        sys.stdout.write('\r'+b)
        LIST_ALL_EXCEL_SHEET.append(my_list)


# list all deals from Data Frame
df_to_list(EXCEL_SHEET)



# Change transaction to latin
for el in LIST_ALL_EXCEL_SHEET:
    # print(el)
    if el[7] == 'Купля':
        # print(el[6])
        el[7] = 'Bought'
    elif el[7] == 'Продажа':
        el[7] = 'Sold'
    else:
        print('SOME ERROR IN KIRILITSA')

# Leave only RIZ1
for deal in LIST_ALL_EXCEL_SHEET:
    if deal[4] == 'RIZ1 [ФОРТС фьючерсы]':
        deal[4] = 'RIZ1'
        RESULTED_LIST_EN.append(deal)
        # LIST_ALL_EXCEL_SHEET.remove(deal)

LIST_ALL_EXCEL_SHEET.clear()

# Change Price to int
for price in RESULTED_LIST_EN:
    int_price = price[5][:3] + price[5][4:]
    price[5] = int(int_price)
    # RESULTED_LIST_PRICE.append(price)

COUNT: int = 1
for quantity in RESULTED_LIST_EN:
    quantity[0] = COUNT
    COUNT += 1 





# show result in console
print()
print('LIST_ALL_EXCEL_SHEET len: ', len(LIST_ALL_EXCEL_SHEET))
print('LIST_ALL_EXCEL_SHEET: ', LIST_ALL_EXCEL_SHEET[0:4])
print('RESULTED_LIST_EN len: ', len(RESULTED_LIST_EN))
print('RESULTED_LIST_EN: ', RESULTED_LIST_EN[40:44])
# print('RESULTED_LIST_PRICE len: ', len(RESULTED_LIST_PRICE))
# print('RESULTED_LIST_PRICE: ', RESULTED_LIST_PRICE[0:4])





# Save to file ri_deals.py
def save_deals(deals_list=LIST_ALL_EXCEL_SHEET):
    with open('ri_deals.py', 'w') as f:
        f.write(str(LIST_ALL_EXCEL_SHEET))
        print('Data rewritred and saved to ri_deals.py')

# Save to file ri_deals.py
# save_deals()