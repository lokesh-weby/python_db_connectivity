import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",password="",database="python_db")

def insert(name,age):
    cursor=con.cursor()
    sql="insert into student(NAME,AGE) values (%s,%s)"
    values=(name,age)
    cursor.execute(sql,values)
    con.commit()
    print(" 1 record inserted")
def delete(no):
    cursor=con.cursor()
    cursor.execute("delete from student where ID=%s",(no,))
    con.commit()
    print(cursor.rowcount," deleted successfully")
def show():
    cursor=con.cursor()
    cursor.execute("select * from student")
    result=cursor.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE"]))
    

#Opertion
while True:
    print('''
    Database Operation
    1.Insert
    2.Delete
    3.show
    4.Exit
    ''')
    choice=int(input("Enter Your choice"))
    if(choice==1):
        name=input("Enter your Name")
        age=int(input("Enter you age"))
        insert(name,age)
    elif(choice==2):
        id=int(input("Enter the Id to delete"))
        delete(id)
    elif(choice==3):
        show()
    elif(choice==4):
        quit()
    else:
        print("Invalid Input")
