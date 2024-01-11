import datetime
import pandas as pd
import os
# import time
import sys

# Path to file
try:
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "D:/Dropbox/TRADING/_deals_for_python/ri_221021.xlsx"
    # rel_path = home/...
    abs_file_path = os.path.join(script_dir, rel_path)
except:
    print('I cand find Excel file')

# reading excel file
start_time = datetime.datetime.now()
print('\n\n\nStart reading excel file...')
EXCEL_SHEET = pd.read_excel(abs_file_path, sheet_name='Лист1',
                        names=[
                            'count_num', 'num', 'date',
                            'ses_date','time', 'instrument',
                            'price', 'quantity', 'volume', 'transaction'
                        ],
                        converters={
                            "price": str
                        })
end_time = datetime.datetime.now()
time_delta = end_time - start_time
print("Reading finished. It's took: ", time_delta.seconds, ' seconds')


# list all deals from Data Frame
# Be aware, we are taking not all columns from excel file
def df_to_list(excel_sheet=EXCEL_SHEET):
    list_all_excel_sheet: list = []
    for index, rows in excel_sheet.iterrows():
        # print(index, rows)
        # rows.num
        my_list: list = [rows.count_num, rows.date,
                        rows.ses_date, rows.time,
                        rows.instrument, rows.price,
                        rows.quantity, rows.transaction]
        b = ("Transfer to list from Pandas Data Frame: " + str(my_list[0]))
        sys.stdout.write('\r'+b)
        list_all_excel_sheet.append(my_list)
    return list_all_excel_sheet





def convert_data_forDB(deals_from_excel):
    resulted_list: list = []
    # Change transaction to latin
    
    # This is conver pandas.timestamp to datetime.datetime
    # fmt = '%Y-%m-%d %H:%M:%S'
    # for date_el in deals_from_excel:
    #     need_to_change = str(date_el[1])
    #     # print(type(date_el[1]))
    #     date_el[1] = datetime.datetime.strptime(need_to_change, fmt)
    #     # print(type(date_el[1]))
    #     date_el[2] = datetime.datetime.strptime(need_to_change, fmt)

    # for date_el in deals_from_excel:

    
    for el in deals_from_excel:
        # print(el)
        if el[7] == 'Купля':
            # print(el[6])
            el[7] = 'Bought'
        elif el[7] == 'Продажа':
            el[7] = 'Sold'
        else:
            print('SOME ERROR IN KIRILITSA')

    # Leave only RIZ1
    for deal in deals_from_excel:
        if deal[4] == 'RIZ1 [ФОРТС фьючерсы]':
            deal[4] = 'RIZ1'
            resulted_list.append(deal)


    # Change Price to int
    for price in resulted_list:
        int_price = price[5][:3] + price[5][4:]
        price[5] = int(int_price)

    COUNT: int = 1
    for quantity in resulted_list:
        quantity[0] = COUNT
        COUNT += 1 
    
    return resulted_list

# list all deals from Data Frame
# deals_from_excel = df_to_list(EXCEL_SHEET)

resulted_list = convert_data_forDB(df_to_list(EXCEL_SHEET))

# show result in console
# print()
print('resulted_list type: ', type(resulted_list))
print('\nresulted_list len: ', len(resulted_list))
print('\nresulted_list: \n', resulted_list[0:4], end='\n')



# Save to file ri_deals.py
# def save_deals(deals_list):
#     with open('ri_deals.py', 'w') as f:
#         f.write(str(deals_list))
#         print('Data rewritred and saved to ri_deals.py')

# Save to file ri_deals.py
# save_deals()