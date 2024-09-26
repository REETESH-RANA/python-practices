# len() used for find out length of string
# k="it's owl streching time"
# print(len(k))

# sorted()
# k="it's owl streching time"
# print(sorted(k))

# k="harry"
# print(sorted(k))
# print(sorted(k,reverse=True))

# center(width,fill_char) it return stringinto the center of the lineand filled left right  spaces with specified characters
# x="PS-SOFTECH"
# k=x.center(23,'$')
# print(k)

# ljust() and rjust() these are also the similar function used to left justify and right justify the string and
#  also filled the remaining spaces with the  specified cahracters
# x="PS-SOFTECH"
# k=x.ljust(15,'*')
# print(k)

# x="PS-SOFTECH"
# k=x.rjust(15,'*')
# print(k)

# only visible last 4 digits of numbers
# x="2232-2344-8978-9897"
# k=x[15:].rjust(19,'*')
# print(k)

#  endswith('pattern',[si],[ei])this  method will return true if string ends with specified paattern otherwise false
# x='jaipur'
# k=x.endswith('pur',1,7)
# print(k)

# x = ("jaipur","rajesthan","kanpur","gwalior","udaipur")
# # for city in x:
# #     if(city.endswith("an")):
# #         print(city)
# # for city in x:
# #     if(city.startswith("j")):
# #         print(city)


# x= "the man the machine the python"
# k=x.rfind("the")
# print(k)
# k=x.rfind("the")
# print(k)

# x="hari prasad sharma"
# k=x[x.find(" ")+1:x.rfind(" ")]
# print(k)

# the use of the split function
# x="ankit,alia,monu,rohit"
# k=x.split(",")
# print(k)
# print(k[3])

# x = "12-jan-2024;reetesh;25:23;1;23"
# k=x.split(";")
# print(k)

# k=x.split(";",1)
# print(k)


# k=x.rsplit(";",1)
# print(k)


