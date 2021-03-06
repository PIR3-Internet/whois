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


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"../pythonsqlite17000.db"

    #all domains with their registrar
    sql_create_table1 = """CREATE TABLE IF NOT EXISTS data_registrar (
                                    domain text PRIMARY KEY,
                                    registrar text NOT NULL
                                );"""

    #all registrar and the quantity of domains 
    sql_create_table2 = """CREATE TABLE IF NOT EXISTS all_registrar (
                                    registrar text PRIMARY KEY,
                                    quantity text NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create tables
        create_table(conn, sql_create_table1)
        create_table(conn, sql_create_table2)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()