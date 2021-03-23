import sqlite3

def create():
    con = sqlite3.connect("oyo.db")
    con.execute("CREATE TABLE IF NOT EXISTS OYO (NAME TEXT, PRICE INT, ADDRESS TEXT, RATINGS TEXT, AMINITIES TEXT)")
    con.close()

def insert(values):
    con = sqlite3.connect("oyo.db")
    sql = "INSERT INTO OYO VALUES (?, ?, ?, ?, ?)"
    con.execute(sql,values)
    con.commit()
    con.close()

def print_details():
    con = sqlite3.connect("oyo.db")
    cur = con.cursor()
    cur.execute("select * from OYO")
    table_data = cur.fetchall()
    for i in table_data:
        print(i)
    con.close()