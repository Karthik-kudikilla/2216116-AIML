import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into participants values(22161011,'shravani','cseai','Btech')")
conn.execute("insert into participants values(22161012,'princy','cseai','Btech')")
conn.execute("insert into participants values(22161013,'naga','cseai','Btech')")
conn.commit()
conn.close()