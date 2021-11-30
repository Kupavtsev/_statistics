from datetime import datetime

result = []
# counter_perevorot_list: list = []

def each_deal_list(deals):
    # global counter_perevorot
    prepared: list = deals

    # counter_perevorot: int = 0

    # All this vars only in case we have open position from first deal
    instrument  = prepared[0][2]
    side        = prepared[0][3]
    quantity    = prepared[0][6]
    enter_price = prepared[0][5]
    commission  = prepared[0][7]
    open_date   = prepared[0][0]
    close_date  = prepared[1][0]
    open_time   = prepared[0][1]
    close_time  = prepared[1][1]
    format      = '%H:%M:%S'
    # deal_result = prepared[1][5] - enter_price if side == 'Bought' else enter_price - prepared[1][5]
    # print(prepared[0:2])
    try:
        # checking instrument to be same
        if instrument == prepared[1][2]:
            # print('the same instrument', prepared[0][2])
            
            # checking for transaction side
            if side != prepared[1][3]:
                # print('This two deals opposite')
                
                # checking for quantity in this deals
                if quantity == prepared[1][6]:
                    # print('We have the same quantity')
                    # Calculations for total closed deal information

                    deal_result = prepared[1][5] - enter_price if side == 'Bought' else enter_price - prepared[1][5]
                    time_in_position = datetime.strptime(close_time, format) - datetime.strptime(open_time, format)
                    
                    finished_deal = {
                        'instrument': instrument,
                        'open_date' : open_date,
                        'close_date': close_date,
                        'open_time' : open_time,
                        'close_time': close_time,
                        'time_in_position' : time_in_position,
                        'side' : side,
                        'quantity' : quantity,
                        'enter_price' : enter_price,
                        'exit_price' : prepared[1][5],
                        'deal_result'    : deal_result,
                        'commission' : commission + prepared[1][7]
                    }

                    # print('finished_deal', finished_deal)
                    result.append(finished_deal)

                    prepared.pop(0)
                    prepared.pop(0)
                    # print('After deal making',prepared[0:2])
                
                # checking for quantity in this deals again
                elif prepared[0][6] != prepared[1][6]:
                    # This situation means Perevorot!
                    if prepared[0][6] < prepared[1][6]:

                        # counter_perevorot += 1
                        # counter_perevorot_list.append(counter_perevorot)
                        # print('counter_perevorot ',counter_perevorot)
                        # print('counter_perevorot_list ',counter_perevorot_list)

                        deal_result = prepared[1][5] - enter_price if side == 'Bought' else enter_price - prepared[1][5]
                        time_in_position = datetime.strptime(close_time, format) - datetime.strptime(open_time, format)
                    
                        finished_deal = {
                            'instrument': instrument,
                            'open_date' : open_date,
                            'close_date': close_date,
                            'open_time' : open_time,
                            'close_time': close_time,
                            'time_in_position' : time_in_position,
                            'side' : side,
                            'quantity' : quantity,
                            'enter_price' : enter_price,
                            'exit_price' : prepared[1][5],
                            'deal_result'    : deal_result,
                            'commission' : commission + prepared[1][7]
                        }

                        # print('finished_deal', finished_deal)
                        result.append(finished_deal)

                        prepared[1][6] = prepared[1][6] - quantity
                        prepared.pop(0)
                        # Next one I need to change

                    # If opend position didnt close in next deal
                    elif prepared[0][6] > prepared[1][6]:
                        pass
        else:
            pass
            print('This is not RIZ1')
    except:
        print('THERE IS NO CORRECT CASE FOR THIS ONE')


def save_deals(result):
    with open('result.py', 'w') as f:
        # You need to make writing from 4th string
        f.write(str(result))
        print('Data rewritred and saved to deals.py')



if __name__ == '__main__':
    from deals import deals
    resulted_deals = each_deal_list
    # print('counter_perevorot_list ',counter_perevorot_list)
    counter = len(deals)/2 + 5
    print('counter', counter)
    while counter>1:
        resulted_deals(deals)
        counter -= 1
        # print(counter)
    # print('The result of function',resulted_deals)
    # print('Result out of the function: ', result)

    # save_deals(result)
