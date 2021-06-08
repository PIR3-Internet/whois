import sqlite3
from sqlite3 import Error


def create_connection(db_file):
   
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_data(conn, data):
 
    sql = ''' INSERT INTO all_registrar(registrar, quantity)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"../pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        # data
        data1 = ('MarkMonitor',25)

        # create tasks
        create_data(conn, data1)


if __name__ == '__main__':
    main()