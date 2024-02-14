from mysql import connector as conn

mydb =conn.connect(host="localhost",user="root",passwd="1234",database="harshil")
mycursor = mydb.cursor()

# mycursor.execute("show tables")
mycursor.execute("insert into ganpat value('meet',19)")
# mycursor.execute("select * from ganpat")
mydb.commit()
for i in mycursor:
    print(i)
