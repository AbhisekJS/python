import mysql.connector as mysql
from mysql.connector import Error

def connect():
    none = None
    try:
        conn=mysql.connect(host='localhost',database='mydbs',user='root',password='testrun')
        
        if conn.is_connected():
            print ("Connected to server")
    except Error as e:
        print(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__=='_main_':
    connect()
