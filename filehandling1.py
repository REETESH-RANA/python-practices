F=open("f:/drinks.txt","a")
while(True):
   v=input("enter the drink name:")
   if(v==''):break
   F.write(v+"\n")
F.close()