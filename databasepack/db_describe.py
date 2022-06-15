import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
'''
    query -> 
'''
str=conn.execute("pragma table_info('participants')")
print(str)
for i in  str:
    print(i)