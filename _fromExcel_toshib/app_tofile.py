import pandas as pd

#
EXCEL_SHEET = pd.read_excel('deals.xlsx', sheet_name='Sheet1',
                      converters={"time": str, "price" : int})


LIST_ALL_EXCEL_SHEET: list = []
RESULTED_LIST_EN: list = []

def df_to_list(excel_sheet=EXCEL_SHEET):
    for index, rows in excel_sheet.iterrows():
        # print(index, rows)
        my_list: list = [rows.date, rows.time,
                        rows.fin_inst_abb, rows.transaction,
                        rows.account, rows.price,
                        rows.quantity, rows.fm_commission]
        LIST_ALL_EXCEL_SHEET.append(my_list)


df_to_list(EXCEL_SHEET)
for el in LIST_ALL_EXCEL_SHEET:
    if el[3] == 'Купля':
        el[3] = 'Bought'
    elif el[3] == 'Продажа':
        el[3] = 'Sold'
    else:
        print('SOME ERROR IN KIRILITSA')
# print('Len of all EXCEL_SHEET: ', len(LIST_ALL_EXCEL_SHEET))
# print(LIST_ALL_EXCEL_SHEET[0:4])

# Save to file deals.py
def save_deals(deals_list=LIST_ALL_EXCEL_SHEET):
    with open('deals.py', 'w') as f:
        f.write(str(LIST_ALL_EXCEL_SHEET))
        print('Data rewritred and saved to deals.py')

# save_deals()