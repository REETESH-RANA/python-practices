# 5. Write a Python program to get a single string from two given strings, separated by a space and
#  swap the first two characters of each string.  
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
  
str1=input("enter the first string:")
str2=input("enter the second string:")

str3=str1+" "+str2
print(str3)
str3=str1[0]+str1[1].replace(str2[0:2],)


        # PROBLEM