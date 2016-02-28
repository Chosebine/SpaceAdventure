import core
import sqlite3

conn = sqlite3.connect('space.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS size
             (name text, sizeModif integer, targetingSys integer, autopilot integer, length real, weight real)''')

c.execute('''CREATE TABLE IF NOT EXISTS starshipType
             (name text, description text, fightingSquare real)''')

sizes = [('Huge', -2, 1, 1, 32, 32000),
         ('Gargantuan', -4, 2, 2, 64, 25000),
         ('Colossal', -8, 3, 3, 256, 1000000),
         ]

starshiptypes = [('Ultralight', 'An ultralight starship can be up to 250 feet long. It occupies a 250-foot-by-250-foot fighting space, and up to four ultralight starships can occupy a single 500-foot square',0.25),
                ('Light', 'A light starship measures 251–500 feet in length. It has a 500-foot-by-500-foot fighting space and occupies a single 500-foot square', 1),
                ('Mediumweight', 'A mediumweight starship measures 501–1,000 feet in length. It occupies a 1,000-foot-by-1,000-foot fighting space (4 500-foot squares)', 4),
                ('Heavy', 'A heavy starship measures 1,001–1,500 feet long. It has a 1,500-foot-by-1,500-foot fighting space (9 500-foot squares).', 9),
                ('Superheavy', 'A superheavy starship is 1,501 feet long or longer. The smallest superheavy starships (measuring 1,501–2,000 feet long) have a 2,000-foot-by-2,000-foot fighting space (16 500-foot squares), although larger fighting spaces are possible.', 16),
                ]
#c.executemany('INSERT INTO starshipType VALUES (?,?,?)', starshiptypes)
c.execute('SELECT * FROM size')
print(c.fetchall())
#for a in range(c.arraysize):

c.execute('SELECT * FROM starshipType')

print(c.fetchone())
conn.commit()
conn.close()
