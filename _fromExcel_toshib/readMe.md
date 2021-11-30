1. My Deals
app_tofile.py
    It's reading excel file (DEALS.XLSX) with my deals and put result to file DEALS.PY as list.
    It would contain all deals, like open and Close postion

app.py 
    Importing deals.py, convert data for database structure and save it in RESULT.PY as list
    It's contain only sign about deal in the list


2. Market Deals
tofile_ri_tape.py
    Reading excel file with deals of RI from Quik
    Convert to latin and to INT what is necessary
    Also it can save data to file...

3.
connect_db.py
    Getting data from tofile_ri_tape.py and put this data to postgresQL

    MultiMon
    ri_211021 done
    ri_221021 done