import psycopg2
import datetime
from pandas import Timestamp

# from account import user_login, user_pass
from config import PG_LOGIN, PG_PASSWORD

resulted_list = [
    [1, Timestamp('2021-10-19 00:00:00'), '2021-10-19 00:00:00', datetime.time(19, 0, 1), 'RIZ1', 189400, 1 , 'Bought'],
    [2, Timestamp('2021-10-19 00:00:00'), '2021-10-19 00:00:00', datetime.time(18, 10, 11), 'RIZ1', 189550, 1 , 'Sold']
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
        count_num = el[0]
        date = el[1]
        ses_date = el[2]
        time = el[3]
        instrument = el[4]
        price = el[5]
        quantity = el[6]
        transaction = el[7]

        cur.execute( # 'cur' object calls the 'execute' method 
            """INSERT INTO public.rts_future_deals(
                count_num, date, ses_date, time, instrument, price, quantity, transaction) VALUES (
                    %(count_num)s,
                    %(date)s,
                    %(ses_date)s,
                    %(time)s,
                    %(instrument)s,
                    %(price)s,
                    %(quantity)s,
                    %(transaction)s
                )""",
                {
                'count_num' : count_num,
                'date' : date,
                'ses_date' : ses_date,
                'time' : time,
                'instrument' : instrument,
                'price' : price,
                'quantity' : quantity,
                'transaction' : transaction,
                }
        )
    conn.commit()

    cur.close()
    conn.close()
    print('Done ok. 200')


if __name__ == '__main__':
    add_to_base(resulted_list)