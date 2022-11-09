# import sqlite3 
# b = sqlite3.connect("Odam.db")
# a = b.cursor()
# a.execute('''
# CREATE TABLE IF NOT EXISTS Odam(
#     ism STRING
#     familiya STRING
#     yosh INTEGER
#     vazn FLOAT 
# )
# ''')

# import sqlite3
# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute('''
# CREATE TABLE IF NOT EXISTS Odam(
#     ism STRING
#     familiya STRING
#     yosh INTEGER
#     vazn FLOAT 
# )
# ''')


import sqlite3 as sql
aa = sql.connect("main.db")
malumot = aa.cursor()
malumot.execute('''
CREATE TABLE IF NOT EXISTS odamlar(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
)
''')

