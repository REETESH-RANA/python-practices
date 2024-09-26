class Person:
    def Getperson(self):
        self.__name=input("Enter name:")
        self.__age=int(input("Enter age:"))
    def Putperson(self):
        print(self.__name,self.__age)
    def Elder(self,T):
        if(self.__age>T.__age):
            return self
        else:
            return T
    
p1=Person()
p1.Getperson()
p1.Putperson()

p2=Person()
p2.Getperson()
p3=p1.Elder(p2)
print('Result:')
p3.Putperson()