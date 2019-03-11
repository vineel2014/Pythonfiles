import sqlite3

def main():
    
    db = sqlite3.connect('test2.db') #Create Database
    
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    
    db.execute('insert into test (t1,i1) values (?,?)',('one',1))
    db.execute('insert into test (t1,i1) values (?,?)',('two',2))
    db.execute('insert into test (t1,i1) values (?,?)',('three',3))
    db.execute('insert into test (t1,i1) values (?,?)',('four',4))
    db.execute('insert into test (t1,i1) values ("five",5) ')
    
    db.commit()
    
    cursor = db.execute('select * from test order by i1')
    
    for x in cursor:
        print(x)
        
    
if __name__ == "__main__": main()
