# # to calculate the length of the string
# x="""'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
# """
# print(len(x))

# 2. Write a Python program to count the number of characters (character frequency) in a string.  Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# string = "google.com"
# for i in string:
#     k=string.count(i)
#     print("'",i,"'",": ",k,end=",")


# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#  If the string length is less than 2, return instead of the empty string.  Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
# str = input("enter the string:")
# if(len(str)>=2):
#     print(str[0:2]+str[-2:])
# else:
#     print("empty string")

# 4. Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed  to '$', except the first char itself.  Sample String : 'restart'
# Expected Result : 'resta$t'
# str = "restart"
# replaced=str[0]+str[1:].replace("r","$")
# print(replaced)

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.  
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
# str=input("enter the string:")
# if(str.endswith("ing")):
#     str=str+"ly"
#     print(str)
# elif(len(str)>=3):
#     str=str+"ing"
#     print(str)
# elif(len(str)<3):
#     print(str)

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.  
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
# t=('excel','access','powerpoint','word')
# x=()
# for i in t:
#     k=len(i)
#     x+=(k,)
# # print(x)
# m=x.index(max(x))
# longest_word=t[m]
# print(longest_word)

# 9. Write a Python program to remove the nth index character from a nonempty string.  
# str = input("Enter a string:")
# n = int(input("enter the index:"))
# str1 = str[:n]+str[n+1:]
# print(str1)

# 11. Write a Python program to remove the characters which have odd index values of a given string.  
# str="the man the machine the python"
# str1 = str[::2]
# print(str1)  

# 12. Write a Python program to count the occurrences of each word in a given sentence.  
# str="the man the machine"
# y=text.split(" ")
# print()

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.  
# str=input("Enter the text:")
# print("YOUR TEXT IN UPPER CASE IS ",str.upper())
# print("YOUR TEXT IN LOWER CASE IS ",str.lower())

# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).  
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
# str="red, white, black, red, green, black"
# str1=str.split()
# u=()
# for v in str1:
#     if(v not in u):
#         u+=(v,)
# print(sorted(u))

# 15. Write a Python function to create the HTML string with tags around the word(s).  
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
# str='i Python'
# y=str.split()
# print(y)
# x=""
# for w in str:
#     x=x+("<"+ w +">")   problem
# print(x)

# 16. Write a Python function to insert a string in the middle of a string.  
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
# str = input("enter the string:")
# str1=input("enter the string to be added:")
# if(len(str)%2==1):
#     midd_ind = len(str)//2
#     result=str[:midd_ind]+str1+str[midd_ind:]
# else:
#     midd_ind = len(str)//2
#     result=str[:midd_ind]+str1+str[midd_ind:]

# print(result)
   
   # 17. Write a Python function to get a string made of 4 copies of the last two characters
#  of a specified string (length must be at least 2).  
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
# not a function but only a program to perform that task
# str=input("enter the string:")
# i=4
# print(str[-2:]*i)

# 18. Write a Python function to get a string made of its first three characters of a specified string. 
# If the length of the string is less than 3 then return the original string.  
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt
# str=input("enter the string: ")
# if(len(str)<3):
#     print(str)
# else:
#     print(str[0:3])

# 19. Write a Python program to get the last part of a string before a specified character.  
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
# str=input("enter the string:")
# s = (input("enter the last character:"))
# last_chr=str.index(s)
# for i in range(0,len(str)):
#     if(str.index(s)==i):
#         print("index of your last character:",i)
# print(str[last_chr+1:])      

# 20. Write a Python function to reverses a string if it's length is a multiple of 4.  
# str=input("enter the string : ")
# if(len(str)%4==0):
#     print(str[::-1])
# else:
#     print("length of string is not multiple of 4")

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase 
# characters in the first 4 characters.  
# str="hELLo"
# count=0
# for v in str[0:4]:
#     if(v.isupper()):
#         count+=1
#         if(count==2):
#             break
#         if(count==2):
#           str.upper()
# print(str)

# 22.Write a Python program to sort a string lexicographically.  
# str="the main written part of a book, newspaper, etc"
# str = str.split()
# k=sorted(str)
# print(k)

# 24. Write a Python program to check whether a string starts with specified characters.  
# str=input("enter the string:")
# specified_char=input("enter the specified characters to be checked:")
# print(str.startswith(specified_char))


# 27. Write a Python program to remove existing indentation from all of the lines in a given text.  
# str="the main written part of a book, newspaper, etc"
# str = str.split()
# k=" ".join(str)
# print(str)

# 30. Write a Python program to print the following floating numbers upto 2 decimal places.  
# x=187.8768
# k="{0:.2f}\n".format(x)
# print(k)

# 31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.  
# x=-187.8768
# k="{0:.2f}\n".format(x)
# print(k)

# 32. Write a Python program to print the following floating numbers with no decimal places.  
# x=86.17
# k="{:0.0f}".format(x)
# print(k)

# 33. Write a Python program to print the following integers with zeros on the left of specified width. 
# str="13" 
# k=str.rjust(10,"0")
# print(k)

# 34. Write a Python program to print the following integers with '*' on the right of specified width.  
# str="13" 
# k=str.ljust(10,"*")
# print(k)

# 35. Write a Python program to display a number with a comma separator
# i=1
# while(i<=5):
#     n=int(input("Enter the no"))
#     print(i,end=',')
#     i=i+1

# 36. Write a Python program to format a number with a percentage
# x=0.98
# k="{:.2%}".format(x)
# print(k)

# 37. Write a Python program to display a number in left, right and center aligned of width 10.  
# x=(input("enter any number :"))
# k=x.ljust(10)
# print(k)
# k=x.rjust(10)
# print(k)
# k=x.center(10)
# print(k)
# k=x.center(10,"*")
# print(k)

# 38. Write a Python program to count occurrences of a substring in a string
# str=input("enter a string:")
# for i in str:
#     k=str.count(i)
#     print(i,":",k)

# 39. Write a Python program to reverse a string.  
# str=input("enter a string: ")
# print(str[::-1])

# 40. Write a Python program to reverse words in a string
# str="the main written part of a book, newspaper, etc"
# str1=str.split()
# str1.reverse()
# str1=" ".join(str1)
# print(str1)

# 41. Write a Python program to strip a set of characters from a string. 
# str="the main written part of a book, newspaper, etc"
# # print(len(str))
# y=str.strip()
# print(len(str))
# print(len(y))
# print(y)  doubt

# 43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.  
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
# str1="The area of the rectangle is 1256.66cm2"
# p=str1[0:len(str1)-1]+chr(178)
# print(p)

# 44. Write a Python program to print the index of the character in a string.  
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9
# str="the man"
# for i in str:
#     k=str.index(i)
#     p="current character %c at %d"%(i,k)
#     print(p)

# 45. Write a Python program to check whether a string contains all letters of the alphabet.  
# str="the main written part of a book newspaper etc"
# print(str.isalpha())
# str1=str.split()
# str2="".join(str)
# print(str2.isalpha())

# 46. Write a Python program to convert a given string into a list of words.  
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# str="the quick brown fox jumps over the lazy dog"
# str=str.split()
# print(str)

# # 47. Write a Python program to lowercase first n characters in a string.  
# str=input("enter the string: ")
# n=int(input("enter the nth index: "))
# for i in range(0,len(str)):
#     if(n==i):
#         print("index of your last character:",i)
# print(str[:n].lower()+str[n:]) 

# 48. Write a Python program to swap comma and dot in a string.  
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
# str="32.054,23"
# t=str.replace(".",",",1)
# print(t)problem

# 51. Write a Python program to find the first non-repeating character in given string.  
# str="the mal the machine the python"
# u=""
# count=0
# for v in str:
#     k=str.count(v)
#     if(k==1):
#         u=u+v
# print(u[0])

# 53. Write a Python program to find the first repeated character in a given string.  
# str="the mal the machine the python"
# u=""
# count=0
# for v in str:
#     k=str.count(v)
#     if(k>1):
#         u=u+v
# # print(u)
# print(u[0])

# 55.Write a Python program to find the first repeated word in a given string.  
# str ="the main written main part of the a book newspaper"
# u=""
# count=0
# for word in str:
#     k=str.count(word)
#     if(k>1):
#         u=u+word
# print(u)
# u=u.split()
# print(u[0])

# 56. Write a Python program to find the second most repeated word in a given string.  
# str ="the main written main part of the a book newspaper"
# u=""
# count=0
# for word in str:
#     k=str.count(word)
#     if(k>1):
#         u=u+word
# print(u)
# u=u.split()
# for i in u:  problem
   
# print(u[0])


# 57.Write a Python program to remove spaces from a given string.  
# str="the main written part of a book newspaper etc"
# str=str.split()
# str1="".join(str)
# print(str1)

# 58. Write a Python program to move spaces to the front of a given string.  
# str="the main written part of a book newspaper etc"
# str=str.rsplit()
# str1="".join(str)
# print(str1)


# 61. Write a Python program to remove duplicate characters of a given string
# str="hellobro"
# str="the man the machine the python"
# str=str.split()
# u=()
# for v in str:
#     if(not v in u):
#         u+=(v,)
# print(u)

# 62. Write a Python program to compute sum of digits of a given string.  
# str=input("enter the string: ")
# digit_sum=0
# for v in str:
#    if v.isdigit():
#       digit_sum+=int(v)
# print("digit_sum is ",digit_sum)

# 63. Write a Python program to remove leading zeros from an IP address.  
# ip_addr = input("enter the ip address: ")
# k=ip_addr.split(".")
# u=()
# for v in k:
#    i=str(int(v))
#    u+=(i,)
# ip=".".join(u)
# print(ip)

# 64. Write a Python program to find maximum length of consecutive 0's in a given binary string.  
# str=input("enter the  binary string: ")
# for i in str:
#    k=str.count("0")
# print(k)

# 67. Write a Python program to remove all consecutive duplicates of a given string.  
# str="the the man the machine the python"
# str=str.split()
# u=()
# for v in str:
#     if(not v in u):
#         u+=(v,)
# print(u)

# 68. Write a Python program to create two strings from a given string. Create the first string using those character
# which occurs only once and create the second string which consists of multi-time occurring characters in the said string.  
# str=input("enter a string: ")
# str=str.split()
# u=()
# w=()
# for v in str:
#     if(not v in u):
#         u+=(v,)
#     else:
#          w+=(v,)
# str1=" ".join(u)
# str2=" ".join(w)
# print(str1)
# print(str2)

# 70.Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings. 
# str1 = input("enter the first string: ")
# # str2 = input("enter the second string: ")
# # str1=str1.split()
# # str2=str2.split()
# u=""
# # count=0
# for word in str1:
#     k=str.count(word)   problem
#     print(word)
#     if(k==1):
#         u=u+word
# print(u)

# 79. Write a Python program to find smallest and largest word in a given string. 
# str="the man the machine the python"
# str=str.split()
# u=()
# for i in str:
#     k=len(i)
#     u+=(k,)
# m=max(u)
# print(m)
# p=str[u.index(m)]
# print(p)
# mi=min(u)
# pr=str[u.index(mi)]
# print(pr)

# 81. Write a Python program to find the index of a given string at which a given substring starts.
#  If the substring is not found in the given string return 'Not found'.  
# str = input("Enter the  string: ")
# substring = input("Enter the substring to find: ")
# index = str.find(substring)
# if index != -1:
#     print(f"The substring '{substring}' starts at index: {index}")
# else:
#     print(f"The substring '{substring}' is not found in the main string.")

