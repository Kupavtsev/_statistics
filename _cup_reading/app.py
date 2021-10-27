import time

"""
I need to read excel file to Pandas DataFrame
Make dict of this data
Append this dicts to list
Save this list to file for some time interval, ex 1M or 10M or so on...
"""

def f():
    print('This is your one second interval')

start_time = time.time()
interval = 1
for i in range(20):
    time.sleep(start_time + i*interval - time.time())
    f()