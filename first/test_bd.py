import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    queri = """ 
  select * from
    netflix 
    limit 2
    
    """
    cursor.execute(queri)

    for row in cursor.fetchall():
        print(row)