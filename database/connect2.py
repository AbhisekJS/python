from mysql.connector import MySQLConnection,Error
from python_mysql_dbconfig import read_db_config

def connect():
    db_config=read_db_config()
    conn=None
    try:
        print('Connecting to MySql database...')
        conn=MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection successful')

        else:
            print('connection failed')
    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('connection closed')

if __name__=='__main__':
    connect()