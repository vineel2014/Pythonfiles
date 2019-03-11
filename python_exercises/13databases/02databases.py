import sqlite3

def main():
    
    db = sqlite3.connect('test1.db') #Create Database
    
    db.row_factory = sqlite3.Row # allows to specify how the rows will be returned
    
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    
    db.execute('insert into test (t1,i1) values (?,?)',('one',1))
    db.execute('insert into test (t1,i1) values (?,?)',('two',2))
    db.execute('insert into test (t1,i1) values (?,?)',('three',3))
    db.execute('insert into test (t1,i1) values (?,?)',('four',4))
    
    db.commit()
    
    cursor = db.execute('select * from test order by i1')
    
    for row in cursor:
        print(row) #returns iterables
        print(dict(row))
        print(list(row))
        print(row['t1'],row['i1'])
        print(row[0],row[1])
    
if __name__ == "__main__": main()
