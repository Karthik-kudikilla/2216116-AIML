import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
query='''
        create table participants(g_id int primary key,name text not null,branch text not null,study text not null)
      '''
conn.execute(query)
