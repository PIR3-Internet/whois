import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def select_all_data(conn):
    reg = []
    count = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM all_registrar")
    rows = cur.fetchall()

    for row in rows:
        
        reg.append(row[0])
        count.append(row[1])
    
    return reg,count

def getData(reg,count) :

    data = [0,0,0,0,0,0,0]
    found = False
    rows = ['Markmonitor','Alibaba','eName','GoDaddy','Corporation Service Company','Network Solutions','Others']
    for i in range (len(reg)):
        found = False
        for j in range(len(rows)-1):
            if reg[i]==rows[j]:
                data[j]+=int(count[i])
                found = True
        if found == False:
            data[6]+=int(count[i])


    return data

def graph(dataM, dataA, dataE, dataG, dataC, dataN, dataO):
    print('hello')
    plotdata = pd.DataFrame({
        "Markmonitor":dataM,
        "Alibaba":dataA,
        "eName":dataE,
        "GoDaddy":dataG,
        "Corporation Service Company":dataC,
        "Network Solutions":dataN
        }, 
        index=["1500", "5000", "10000", "17000"]
    )
    plotdata.plot(kind="bar").legend(
                                       loc='best', ncol=3 
    )
    plt.xticks(rotation=30, horizontalalignment="center")
    plt.title("percentages")
    plt.xlabel("nb domains")
    plt.ylabel("Registrars")
    plt.show()




if __name__ == '__main__':
    print("Start")

    database1_5 = r"../pythonsqlite1500.db"
    database5 = r"../pythonsqlite5000.db"
    database10 = r"../pythonsqlite10000.db"
    database17 = r"../pythonsqlite17000.db"

    # create a database connection
    conn = create_connection(database1_5)
    with conn:
        reg1_5, count1_5 = select_all_data( conn)
    conn = create_connection(database5)
    with conn:
        reg5, count5 = select_all_data( conn)
    conn = create_connection(database10)
    with conn:
        reg10, count10 = select_all_data( conn)
    conn = create_connection(database17)
    with conn:
        reg17, count17 = select_all_data( conn)

    data1_5=getData(reg1_5,count1_5)
    data5=getData(reg5,count5)
    data10=getData(reg10,count10)
    data17=getData(reg17,count17)

    print(data1_5)
    
    dataM=[data1_5[0]/1509,data5[0]/5149,data10[0]/10421,data17[0]/18328]
    dataA=[data1_5[1]/1509,data5[1]/5149,data10[1]/10421,data17[1]/18328]
    dataE=[data1_5[2]/1509,data5[2]/5149,data10[2]/10421,data17[2]/18328]
    dataG=[data1_5[3]/1509,data5[3]/5149,data10[3]/10421,data17[3]/18328]
    dataC=[data1_5[4]/1509,data5[4]/5149,data10[4]/10421,data17[4]/18328]
    dataN=[data1_5[5]/1509,data5[5]/5149,data10[5]/10421,data17[5]/18328]
    dataO=[data1_5[6]/1509,data5[6]/5149,data10[6]/10421,data17[6]/18328]

    graph(dataM, dataA, dataE, dataG, dataC, dataN, dataO)


    print("End")