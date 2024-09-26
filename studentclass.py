class student:
    def GetStudents(self):
        self.__rollno=input("Enter the student roll no:")
        self.__name=input("Enter the student name:")
        self.__physics=input("Enter the physics marks:")
        self.__Chemistry=input("Enter the Chemistry marks:")
        self.__Maths=input("Enter the Maths marks:")     
    def ShowStudents(self):
        print(self.__rollno,self.__name,self.__physics,self.__Chemistry,self.__Maths)
    def SearchByRollno(self,rollno):
        if(rollno==self.__rollno):
            self.ShowStudents()
            print("Total",self.__Chemistry+self.__Maths+self.__physics)
            
            return True
        return False
    def SearchByName(self,name):
        if(name==self.__name):
            self.ShowStudents()
            return True
        return False
L=[]
n=int(input("enter the n:"))
for i in range(n):
    C=student()
    C.GetStudents()
    L.append(C)

while(True):
    print("1:show all Students\n2:search by Roll no\n3:Search by name\n4:exit\n")
    ch=input("Enter your choice :")
    if(ch=="1"):
        for c in L:
            c.ShowStudents()
   
   
   
    elif(ch=="2"):
        rollno=(input("enter the roll no you want to search ?:"))
        for c in L:
            found=c.SearchByRollno(rollno)
            if(found):break
        if(not found):
            print("Roll number not existed")
  
    elif(ch=="3"):
        name=(input("enter the name you want to search ?:"))
        for c in L:
            found=c.SearchByName(name)
            if(found):break
        if(not found):
            print("Student name  not existed")
    elif(ch=="4"):
        break
    