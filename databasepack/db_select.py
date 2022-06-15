import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

res=conn.execute("select * from participants")
for i in res:
    print(i)