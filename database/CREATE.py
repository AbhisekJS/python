import mysql.connector;

conn = mysql.connector.connect(host='localhost',database='mydbs',user='root',password='testrun')

if conn.is_connected():
    print("connected to mysql db")

cursor= conn.cursor()

try:
    cursor.execute("insert into emp values(3,'Cobb',12000)")
    conn.commit()
    print("employee added")

except:
    conn.rollback()

'''row= cursor.fetchone()'''

'''while row is not None:
    print(row)
    row=cursor.fetchone()'''



cursor.close()

conn.close()