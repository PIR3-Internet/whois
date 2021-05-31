import sqlite3
from sqlite3 import Error
import csv
import whois

def create_connection(db_file):
   
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_data(conn, data):
 
    sql = ''' INSERT OR IGNORE INTO data_registrar(id, domain, registrar)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def read(file, conn):

    with open(file,'r') as f_in :

        myReader = csv.reader(f_in)
        i=0
        failure = list()
        print("start")

        for row in myReader:
            if i<100:
                
                try:

                    w = whois.query(row[0], ignore_returncode=1)
                    print(row[0])

                    data=(i,row[0],w.registrar)
                    create_data(conn,data)

                except Exception as e:
                    failure.append(row[0])
                    message = """
                    Error : {},
                    On Domain: {}
                    """.format(str(e), row[0])
                    print(message)
            i=i+1


def main():
    database = r"../pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        file="newList3.csv"
        read(file, conn)

if __name__ == '__main__':
    main()