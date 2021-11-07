1.
app_tofile.py
    It's reading excel file (DEALS.XLSX) with my deals and put result to file DEALS.PY as list.
    It would contain all deals, like open and Close postion

app.py 
    Importing deals.py, convert data for database structure and save it in RESULT.PY as list
    It's contain only sing about deal in the list

2.
tofile_ri_tape.py
    Reading excel file with deals of RI from Quik
    Convert to latin and to INT what is necessary
    Also it can save data to file...