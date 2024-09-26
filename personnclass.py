class Person:
    def Getperson(self):
        self.__name=input("Enter name:")
        self.__age=int(input("Enter age:"))
    def Putperson(self):
        print(self.__name,self.__age)
    def __gt__(self,T):
        if(self.__age>T.__age):
            return True
        else:
            return False
    
p1=Person()
p1.Getperson()

p2=Person()
p2.Getperson()

p1.Putperson()
p2.Putperson()

print(p1.__gt__(p2))
if(p1>p2):
    p1.Putperson()
else:
    p2.Putperson()