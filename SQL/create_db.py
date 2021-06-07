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
    database = r"../pythonsqlite.db"


    sql_create_table_data = """CREATE TABLE IF NOT EXISTS data_registrar (
                                    domain text PRIMARY KEY,
                                    registrar text NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create tasks table
        create_table(conn, sql_create_table_data)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()