"""
This is to send my data deals to Postgres
"""

import psycopg2
import datetime
from pandas import Timestamp

# from account import user_login, user_pass
from config import PG_LOGIN, PG_PASSWORD

resulted_list = [
    {'instrument': 'RIZ1', 'open_date': Timestamp('2021-09-28 00:00:00'), 'close_date': Timestamp('2021-09-28 00:00:00'), 'open_time': '10:56:56', 'close_time': '11:09:21', 'time_in_position': datetime.timedelta(seconds=745), 'transaction': 'Bought', 'quantity': 1, 'enter_price': 176450, 'exit_price': 176230, 'deal_result': -220, 'commission': 11.2},
    {'instrument': 'RIZ1', 'open_date': Timestamp('2021-09-28 00:00:00'), 'close_date': Timestamp('2021-09-28 00:00:00'), 'open_time': '11:27:17', 'close_time': '11:29:40', 'time_in_position': datetime.timedelta(seconds=143), 'transaction': 'Bought', 'quantity': 1, 'enter_price': 175510, 'exit_price': 175510, 'deal_result': 0, 'commission': 11.2},
    {'instrument': 'RIZ1', 'open_date': Timestamp('2021-09-28 00:00:00'), 'close_date': Timestamp('2021-09-28 00:00:00'), 'open_time': '11:29:56', 'close_time': '11:32:45', 'time_in_position': datetime.timedelta(seconds=169), 'transaction': 'Bought', 'quantity': 1, 'enter_price': 175470, 'exit_price': 176070, 'deal_result': 600, 'commission': 11.2},
    ]

# To put this number in first brackets
need_it = len(resulted_list)

def add_to_base(dict_my):

    try:
        conn = psycopg2.connect(
            user = PG_LOGIN,
            password = PG_PASSWORD,                           
            database = 'forts',
            host = 'localhost',
            port = 5432,
        )
    except Exception as ex:
        print(' /// ----- I am unable to connect to the database ----- ///', ex)
        raise ex

    cur = conn.cursor()


    for el in dict_my:
        instrument = el['instrument']
        open_date = el['open_date']
        close_date = el['close_date']
        open_time = el['open_time']
        close_time = el['close_time']
        time_in_position = el['time_in_position']
        transaction = el['transaction']
        quantity = el['quantity']
        enter_price = el['enter_price']
        exit_price = el['exit_price']
        deal_result = el['deal_result']
        commission = el['commission']

        cur.execute( # 'cur' object calls the 'execute' method 
            """INSERT INTO public.rts_future_mydeals(
                instrument, open_date, close_date, open_time, close_time,
                time_in_position, transaction, quantity, enter_price,
                exit_price, deal_result, commission
                ) VALUES (
                    %(instrument)s,
                    %(open_date)s,
                    %(close_date)s,
                    %(open_time)s,
                    %(close_time)s,
                    %(time_in_position)s,
                    %(transaction)s,
                    %(quantity)s,
                    %(enter_price)s,
                    %(exit_price)s,
                    %(deal_result)s,
                    %(commission)s
                )""",
                {
                'instrument' : instrument,
                'open_date' : open_date,
                'close_date' : close_date,
                'open_time' : open_time,
                'close_time' : close_time,
                'time_in_position' : time_in_position,
                'transaction' : transaction,
                'quantity' : quantity,
                'enter_price' : enter_price,
                'exit_price' : exit_price,
                'deal_result' : deal_result,
                'commission' : commission
                }
        )
    conn.commit()

    cur.close()
    conn.close()
    print('Done ok. 200')


if __name__ == '__main__':
    add_to_base(resulted_list)