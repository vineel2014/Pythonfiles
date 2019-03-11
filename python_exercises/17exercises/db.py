import MySQLdb

cxn = MySQLdb.connect(host="",db="",user="")
cur = cxn.cursor()
cur.execute("Select * from table where column = 1")
for x in cur.fetchall():
    print(x)

cur.close()
cxn.commit()
cxn.close()