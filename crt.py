from db import connection
conn=connection()
if conn:
    print("connection established successfully")
else:
    print("connection failed")

def insert_data():
    roll_no=int(input("Enter roll number: "))
    name=input("Enter name: ")
    branch=input("Enter branch: ")
             
    cursor=conn.cursor()
    query="insert into student(roll_no,name,branch) values(%s,%s,%s)"
    values=(roll_no,name,branch)
    cursor.execute(query,values)
    conn.commit()
    print("data inserted successfully")
def fetch_data():
    cursor=conn.cursor()
    query="select * from student"
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)

def update_data():
    roll_no=int(input("Enter roll number: "))
    name=input("Enter name: ")
    branch=input("Enter branch: ")
    cursor=conn.cursor()
    query="update student set name=%s, branch=%s where roll_no=%s"
    values=(roll_no,name,branch)
    cursor.execute(query,values)
    conn.commit()
    print("Data updated successfully")
#while loop to perform operations
print("1. insert Data")
print("2. fetch Data")
print("3. update Data")
print("Enter 4 to exit")
while True:
    choice=int(input("Enter your choice (1-4): "))
    if choice==1:
        insert_data()
    elif choice==2:
        fetch_data()
    elif choice==3:
        update_data()
    elif choice==4:
        print("Exiting...")
        break            

