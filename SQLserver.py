import os,pymssql

server="#######"
user="######"
password="#########"

conn=pymssql.connect(server,user,password,database="#####")
cursor=conn.cursor()
cursor.execute("""select getdate()""")
row=cursor.fetchone()
while row:
    print("sqlserver version:%s"%(row[0]))
    print("hello world!")
    row=cursor.fetchone()

conn.close()