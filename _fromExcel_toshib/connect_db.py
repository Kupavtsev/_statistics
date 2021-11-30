import psycopg2
import datetime
# from account import user_login, user_pass
from config import PG_LOGIN, PG_PASSWORD

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

# GETTING DATA FROM DB
    
    # postgreSQL_select_Query = "SELECT * FROM public.anti;"
    # cur.execute(postgreSQL_select_Query)

    # print("Selecting rows from mobile table using cursor.fetchall")
    # mobile_records = cur.fetchall()
    # print('=============================================================')
    # print(mobile_records)
    # print(type(mobile_records))
    # print('=============================================================')

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
    from tofile_ri_tape import resulted_list
    # add_to_base(id, sender, email, send_date)
    add_to_base(resulted_list)