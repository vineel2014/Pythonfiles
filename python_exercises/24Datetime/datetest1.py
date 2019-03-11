import datetime as dt
# date has been entered in dd/mm/yy format
test_date = "15/07/03"
d1 = dt.datetime.strptime(test_date, "%d/%m/%y")
print (d1, type(d1))  # 2003-07-15 00:00:00 <type 'datetime.datetime'>
# convert datetime object to a 10 character string
d2 = str(d1)[:10]
print (d2, type(d2))  # 2003-07-15 <type 'str'>
# now you can use string d2 to create filenames
fname = "data.dat"
new_fname = d2 + fname
print (new_fname)  # 2003-07-15data.dat

