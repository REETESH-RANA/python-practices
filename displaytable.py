import pymysql as MYSQL
try:
 
 cn=MYSQL.connect(host="localhost", user="root", passwd="1234" ,database="Cello")
 smt=cn.cursor()
 q="select * from products"
 smt.execute(q)
 records=smt.fetchall()
 if(len(records)>0):
  #print(records)
  print("Id\t\t%-20s\t\t\t%10s"%("Name","Price"))
  print("------------------------------------------------------------------------------")
  for row in records:
   print("%s\t\t%-20s\t\t\t%10.2f"%(row[0],row[1],row[2]))
 else :
   print("No Record Found")
   cn.close()
except Exception as e:
 print("Error :",e)