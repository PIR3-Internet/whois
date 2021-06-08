import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def delete_data(conn, d):

    sql = 'DELETE FROM data_registrar WHERE domain=?'
    cur = conn.cursor()
    cur.execute(sql, (d,))
    print(d, ' - deleted')
    conn.commit()

def select_all_data(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM data_registrar")

    rows = cur.fetchall()
    x=0
    for row in rows:
        
        reg = row[1]
        if(x>=10000):
            delete_data(conn, row[0])
        
        x+=1
        

if __name__ == '__main__':
    print("Start")

    database = r"../pythonsqlite10000.db"

    # create a database connection
    conn = create_connection(database)

    with conn :
        select_all_data(conn)

    print("End")
