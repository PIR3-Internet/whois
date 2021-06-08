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


#data into database
def create_data(conn, data):
 
    sql = ''' INSERT OR IGNORE INTO data_registrar( domain, registrar)
              VALUES(?,?) '''
    with conn :
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

        #for every domains
        for row in myReader:
            if i<1000000:
                if i>24200:
                    try:

                        w = whois.query(row[0], ignore_returncode=1)    #get registrar
                        reg = w.registrar
                        data=(row[0],reg)
                        create_data(conn,data)                          #data into the database
                        print(row[0],end=' - ')
                        print(reg)

                    except Exception as e:                              #If error
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

        file="list_domains.csv"
        read(file, conn)

if __name__ == '__main__':
    main()