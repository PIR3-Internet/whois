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
 
    sql = ''' INSERT INTO data_registrar(id, domain, registrar)
              VALUES(?,?,?) '''
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
        data1 = (0,'google.com','MarkMonitor Inc.')
        data2 = (1,'youtube.com','MarkMonitor Inc.')

        # create tasks
        create_data(conn, data1)
        create_data(conn, data2)


if __name__ == '__main__':
    main()