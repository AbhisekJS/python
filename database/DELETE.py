import mysql.connector;

def delete(id):
    conn = mysql.connector.connect(host='localhost',database='mydbs',user='root',password='testrun')
    if conn.is_connected():
        print("connected to mysql db")
        cursor= conn.cursor()
        str ="delete from emp where id= '%d'"
        args=(id)

        try:
            cursor.execute(str % args)
            conn.commit()
            print("employee deleted")

        except:
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

empId= int(input('Enter Emp Id: '))
delete(empId)