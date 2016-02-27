import core
import sqlite3

conn = sqlite3.connect('space.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS size
             (name text, sizeModif integer, targetingSys integer, autopilot integer, length real, weight real)''')

sizes = [('Huge', -2, 1, 1, 32, 32000),
         ('Gargantuan', -4, 2, 2, 64, 25000),
         ('Colossal', -8, 3, 3, 256, 1000000),
         ]
# c.executemany('INSERT INTO size VALUES (?,?,?,?,?,?)', sizes)
c.execute('SELECT * FROM size')
print(c.fetchall())
conn.commit()
conn.close()
