# assignment question 2 solution logic
text=" the man the machine [456] the 76 python"
# si=0
# while(True):
#     si=text.find("[",si)
#     if(si==-1):break
#     ei=text.find("]",si+1)
#     if(ei==-1):break
#     print(text[si:ei])


# use that same logic in upper program
# y=text.split(" ")
# print(y)
# for  word in y:
#     if('[' in word):
#       print(word)

# for finding any numeric value in text
# y=text.split(" ")
# c=0
# # print(y)
# for  word in y:
#     if(word.isnumeric()):
#         print(word)
#         c=c+1

# print(c)



# for printing same text with numbers but add 2000 wherever numeric value occurs
# s=""
# word=text.split(' ')

# for w in word:
#     if(w.isnumeric()):
#         w=int(w)+2000
#         s=s+str(w)+" "
#     else:
#         s=s+w+" "

# print(s)