import threading
class car(threading.thread):
    def GetCar(self,name,color):
        self.__name=name
        self.__color=color
    def run(self):
        while(True):
            print(self.__name,self.__color,"Car is running")


C1=Car()
C1=GetCar("Honda",'White')

C2=Car()
C2=GetCar('Verna','Black')

C1.start()
C2.start() 