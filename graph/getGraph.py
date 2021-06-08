import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def select_all_data(reg, count, conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM all_registrar")
    rows = cur.fetchall()

    for row in rows:
        
        reg.append(row[0])
        count.append(row[1])
    
    return reg,count

def graph(reg,count):
    print('hello')

    labels = []
    sizes = []
    labels.append('Others')
    sizes.append(0)

    for i in range (len(reg)):
        if int(count[i])>200:
            labels.append(reg[i])
            sizes.append(int(count[i]))
        else :
            sizes[0]+=int(count[i])


    #colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    #explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)   #patches, texts = 
    #plt.legend(patches, labels, loc="best")
    plt.title('Registrars for 17000 domains\n')
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()




if __name__ == '__main__':
    print("Start")

    database = r"../pythonsqlite17000.db"

    # create a database connection
    conn = create_connection(database)


    reg = []
    count = []

    with conn:
        reg, count = select_all_data(reg, count, conn)

    graph(reg,count)
    

    print("End")