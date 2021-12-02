"""
It's reading excel file (DEALS.XLSX) with my deals and put result to file DEALS.
PY as list.
It would contain all deals, like open and Close postion

DONT'T FORGOT TO OPEN SAVING FUNCTION....


from pandas import Timestamp
deals = ...
"""
import os
import pandas as pd


# Path to file
try:
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "D:/it_locale/python_projects_env/_statistics/_fromExcel_toshib/deals.xlsx"
    abs_file_path = os.path.join(script_dir, rel_path)
except:
    print('I cand find Excel file')


print('\n\n\nStart reading excel file...')
EXCEL_SHEET = pd.read_excel(abs_file_path, sheet_name='Sheet1',
                      converters={"time": str, "price" : int})
print("Reading finished. It's took: ", end='\n')


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