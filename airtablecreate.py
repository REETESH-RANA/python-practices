import pymysql as MYSQL
cn=MYSQL.connect(host="localhost",user="root",passwd="1234",database="flight")
smt=cn.cursor()
 q="Create table flight(flightid int primary key,companyname varchar(50), )
 smt.execute(q)
 print("Table Create Successfully.....")
 cn.commit()
 cn.close()

except Exception as e:
 print("Error :",e)
