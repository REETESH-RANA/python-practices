class Time:
     def GetValues(self):
        self.__h=int(input("Enter the hours:"))
        self.__m=int(input("Enter the minutes:"))
        self.__s=int(input("Enter the hours:"))
    def ShowTime(self):
        print(self.__h,self.__m,self.__s)
    def Add(self,T):
        R=Time()
        R.__h=self.__h+T.__h
        R.__m=self.__m+T.__m
        R.__s=self.__s+T.__s
        return (R)

        R.__m=R.__m+R.__s/60
        R.__s=R.__s%60

        R.__h=R.__h+R.__m/60
        R.__m=R.__m%60

        d=R.__h//24
        print("Days:",d)
        R.__h=R.__h%24

T1=Time()
T1.GetValues()
T1.ShowTime()
T2=Time()
T2.GetValues()
T2.ShowTime()
# incomplete
