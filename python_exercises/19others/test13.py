import sqlite3 as lite

con = lite.connect('user.db')
with con:   
 cur = con.cursor()
 cur.execute("delete from login")
 if cur.fetchall()==[]:
     print("deleted successfully")
 else:
     print("deletion not possible")

print(cur.fetchall())
