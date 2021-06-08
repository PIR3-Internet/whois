from os import cpu_count
import sqlite3
from sqlite3 import Error
from fuzzywuzzy import fuzz


def create_connection(db_file):
   
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_data(tab,count, conn):
 
    cur = conn.cursor()
    cur.execute("SELECT * FROM data_registrar")
    rows = cur.fetchall()
    x=0
    for row in rows:
        reg = row[1]
        found = False
        for i in range(len(tab)) :
            if fuzz.partial_ratio(reg.lower(),tab[i].lower())>=80:
                count[i]=count[i]+1
                found = True
        if found == False :
            tab.append(reg)
            count.append(1)


        
    print(' ')
    return tab,count

def create_data(data,conn): 

    sql = ''' INSERT or IGNORE INTO all_registrar(registrar, quantity)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"../pythonsqlite17000.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        tab= []
        count=[]

        tab,count= get_data(tab,count, conn)

        for i in range(len(tab)):
            print(tab[i],end=' - ')
            print(count[i])
            data =(tab[i],count[i])
            create_data(data,conn)



if __name__ == '__main__':
    main()