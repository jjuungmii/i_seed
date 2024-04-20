#2 
class Car :
    color = ""
    speed = 0
    
    def upSpeed(self, value) : 
        self.speed += value 
        

#4 
class Horse :
    speed = 0
    
    def __init__(self) :
        self.speed = 50 


#6
class Car : 
    def method(self):
        print("슈퍼 클래스")
        
class Sedan(Car) : 
    def method(self): 
        print("서브 클래스")
        
myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

=>3번 수퍼클래스, 서브클래스

#7 
class Car : 
    speed = 0
    
    def upSpeed(self, value) : 
        self.speed = self.speed + value
        
    def setSeatNum(self, num) :
        self.searNum = num
    seatNum = 0
        
    def getSeatNum(self) : 
        return self.seatNum
    

        