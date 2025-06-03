import mysql.connector
def connection():
    conn= mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_managment"
    )
    return conn
if(connection()):
    print("connection established")
else:
    print("connection failed") 