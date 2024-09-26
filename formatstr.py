# use of format command in strings
# x=100
# y=200
# z=x+y
# k="{},{},{}".format(x,y,z)
# k="{0},{1},{2},{1},{0}".format(x,y,z)
# print(k)

# S=[('peter',"12:30 am"),('harry singh',"1:20 pm"),('annkit kumar',"10:30 am")]
# for s in S:
    k="hi {0}\n your interview timming is {1} dated 27 feb 2024\n mr.{0} please join the meeting before half an hour".format(s[0],s[1])
    print(k)


