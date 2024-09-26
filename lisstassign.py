# 1. Write a Python program to sum all the items in a list.  
# l=[6,8,5,6]
# s=0
# for i in l:
#     s=s+i
# print("sum",s)

# 2. Write a Python program to multiplies all the items in a list.  
# l=[6,8,5,6]
# s=1
# for i in l:
#     s=s*i
# print("sum",s)

# 3. Write a Python program to get the largest number from a list.  
# l=[6,8,5,9]
# num=0
# for i in l:
#     if(n>num):
#         num=num
# print(num)

# 4. Write a Python program to get the smallest number from a list.  
# l=[6,8,5,9]
# print(min(l))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and
#  the first and last character are same from a given list of strings.  
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# List = ['abc', 'xyz', 'aba', '1221']
# s=0
# for word in List:
#     if(len(word)>=2) and word[0]==word[-1]:
#         s=s+1
# print(s)

# 7. Write a Python program to remove duplicates from a list.  
# l=[44,87,66,88,55,76,44,66,76,88,88]
# u=[]
# for i in l:
#     t=l.count(i)
#     if(i not in u):
#         u+=(i,)
# print(u)

# 8. Write a Python program to check a list is empty or not.  
# l=[44,87,66,88,55,76,44,66,76,88,88]
# num=0  
# for i in l:
#     num=num+1
# if(num>0):
#     print("element present in list..")
# else:
#     print("list is empty..")

# 9. Write a Python program to clone or copy a list
# l=[44,87,66,88,55,76,44,66,76,88,88]
# t=[]
# t=l.copy()
# print(t)
# or another method
# for i in l:
#     t.append(i)
# print(t)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.  
# l=['hell','hello','monkey','python','gorrilla','dinosaur']
# n=int(input("enter the length of words you want :"))
# for i in l:
#     if(len(i)>n):
#         print(i)


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.  
# l=[44,87,66,88,55]
# m=[43,34,23,88,0]
# for i in l:
#     for v in m:
#         if(i==v):
#             print("TRUE")
        
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# t=l.pop(0)
# t=l.pop(3)
# t=l.pop(3) 
# print(l)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.  
# l=[3,2,4,6,87,88,65]
# t=[]
# for i in l:
#     if(i%2==0):
#         del[i]
#     else:
#         t.append(i)
# print(t)

# 19. Write a Python program to get the difference between the two lists.  
# l=[44,87,66,88,55]
# m=[43,34,23,88,0]
# for i in l:
#     if(i not in m ):
#         print(i)
  
# 20. Write a Python program access the index of a list
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# element = input("enter the element whose index you want to find: ")
# print("your element is present at ",l.index(element))

# 21. Write a Python program to convert a list of characters into a string.  
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# t=" ".join(l)
# print(t)

# 22. Write a Python program to find the index of an item in a specified list
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# element = input("enter the element whose index you want to find: ")
# print("your element is present at ",l.index(element))

# 24. Write a Python program to append a list to the second list.  
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# m=[76,87]
# l.append(m)
# print(l)

# 25. Write a Python program to select an item randomly from a list. 
# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# import random
# random_choice=random.choice(l)
# print(random_choice)

# 27. Write a Python program to find the second smallest number in a list.  
# l=[3,53,32,43,546,34.4,4534,2324,434,4223]
# l.sort()
# print(l)
# print("second smallest number in the list is ",l[1])

# 28. Write a Python program to find the second largest number in a list.  
# l=[3,53,32,43,546,34.4,4534,2324,434,4223]
# l.sort()
# l.reverse()
# print(l)
# print("second largest no. in the list ",l[1])

# 29. Write a Python program to get unique values from a list.  
# l = ['Red', 'Green', 'Red', 'Black', '3','3', 'Yellow','4','34']
# m=[]
# for i in l:
#     if(i not in m):
#         m.append(i)
        # or also we can use this method for directly print the unique values from the list
# print(m)

# 30. Write a Python program to get the frequency of the elements in a list
# l = ['Red', 'Green', 'Red', 'Black', '3','3', 'Yellow','4','34']
# m=[]
# for i in l: 
#     if(i not in m ):
#         m.append(i)
# print(m)
# for v in m:
#     print(v,":",l.count(v))

# 37. Write a Python program to find common items from two lists.  
# l=[44,87,66,88,55]
# m=[43,34,23,88,66]
# for i in l:
#    for v in m:
#         if(i==v):
#             print(i,end=" ")

# 39. Write a Python program to convert a list of multiple integers into a single integer.  
# l=[23,34,23,24,53,353,24]
# t=int(" ".join(l))
# print(t)         prob

# 46. Write a Python program to select the odd items of a list.  
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in list:
#     if(i%2 != 0):
#         print(i)



# 3 in one assignment of tupple,list,and ditcionary : list part
'''1. A magic 8-ball, when asked a question, provides a random answer from a list. The code below contains a list of possible 
answers. Create a magic 8-ball program that asks a question, then gives a random answer.
Example:
import random
L=[5,6,7,8]
Print(random.choice(L))
Will return random no from list.'''
# answers = [ "It is certain", "It is decidedly so", "Without a \ doubt", "Yes, definitely", "You may rely on it",
# "As I see it, \ yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
# "Ask again later", "Better not tell you \ now", "Cannot predict now", "Concentrate and ask again",
# "Don ' t \ count on it", "My reply is no", "My sources say no", "Outlook \ not so good", "Very doubtful" ]
# import random
# question=input("ask your question: ")
# random_answer = random.choice(answers)
# print(random_answer)

'''2] A playing card consists of a suit ("Hearts", "Spades", "Clubs", "Diamonds") and a 
value (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"). Create a list of all possible playing cards,
which is a deck. Then create a func-tion that shuffles the deck, producing a random order.'''
# import random
# ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
# suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# list=[]
# for i in range(0,52):
#         random_rank = random.choice(ranks)
#         random_suits = random.choice(suits)
#         p=(random_rank,"of",random_suits)
#         list.append(p)
# print(list)
# print(random_rank,"of",random_suits)
# random_card = random.choice(list)
# k=" ".join(random_card)
# print(k)
'''
3]  A first-in-first-out (FIFO) structure, also called a “queue,” is a list that gets new elements added at the end,
while elements from the front are removed and processed. Write a program that processes a queue. In a loop,
ask the user for input. If the user just presses the Enter key, the program ends. If the user enters anything else,
except for a single question mark (?), the program considers what the user entered a new element and appends it 
to the queue. If the user enters a single question mark, the program pops the first element from the queue and displays it.
You have to take into account that the user might type a question mark even if the queue is empty.
'''
# l=[]
# while(True):
#         i=input("enter the  item: ")
#         l.append(i)
#         if(i=='?'):
#                 p=l.pop(0)
#                 print('your first item in the list is: ',p)
#                 print("your list is :",l)
#         elif(i==''):
#                 print("your list is: ",l)
#                 exit()

'''4] Count how often each letter occurs in a string(case-insensitively).You can ignore every character that is not a letter.
Print the letters with their counts, in order from highest count to lowest count.'''
