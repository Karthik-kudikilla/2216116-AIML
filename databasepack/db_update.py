import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''update participants set name='chanadana' where g_id=20161012'''
conn.execute(query)
print(conn.total_changes)
conn.commit()
conn.close()