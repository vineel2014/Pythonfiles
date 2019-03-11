import sqlite3 as lite
import sys
 
con = lite.connect('user.db')
 
with con:
    
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Vineel Kumar')")
    cur.execute("INSERT INTO Users VALUES(2,'Kajal')")
    #cur.execute("delete from users")
