import pymysql as MYSQL
try:
 cn=MYSQL.connect(host="localhost",user="root",passwd="1234")
 smt=cn.cursor()
 q="create database flight"
 smt.execute(q)
 print("database created successfully...")
 cn.commit()
 cn.close()
except Exception as e:
 print("ERROR:",e)