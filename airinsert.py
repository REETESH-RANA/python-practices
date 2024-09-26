import pymysql as mysql 
try:
    cn=mysql.connect(host="localhost",user="root",password="1234",database="flight")
    smt=cn.cursor()
    while True: 
        p=input("enter flightid ,companyname , madeby ,source ,destination ,days ,fare ,offer ,totalseats  ,airportsource ,airportdestination ,contactperson ,mobilenumber :").split(',')
        q="insert into flight values ({0},'{1}','{2}','{3}','{4}','{5}',{6},{7},{8},'{9}','{10}','{11}',{12})".format(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12])
        print(q)
        smt.execute(q)
        cn.commit()
        print("record submitted successfully....")
        ch=input("press y to continue...")
        cn.close()
except Exception as e:
    print("error:",e)