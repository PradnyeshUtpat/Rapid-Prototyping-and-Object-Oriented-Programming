from abc import ABC,abstractmethod
from math import sqrt

class Polygon(ABC):
    
    @abstractmethod
    def get_perimeter(self):
        pass
    
    @abstractmethod
    def get_area(self):
        pass
    

class Rectangle(Polygon):
    
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth

    def get_perimeter(self):
        if(self.__length  == self.__breadth):
            print(" \n -----------------it is square----------------- \n")
            print(" \n -----------------Perimeter of square----------------- \n")
            print(2*(self.__length + self.__breadth))
        else:
            print(" \n -----------------Perimeter of Rectangle----------------- \n")
            print(2*(self.__length + self.__breadth))
    def get_area(self):
        if(self.__length  == self.__breadth):
            print(" \n -----------------it is square")
            print(" \n -----------------Area of given sqaure----------------- \n")
            print(self.__length*self.__breadth)
        else:
            print(" \n -----------------Area of Rectangle----------------- \n")
            print(self.__length *self.__breadth);
    
class Triangle(Polygon):
    def __init__(self,side1,side2,side3):
        self.__s1 = side1
        self.__s2 = side2
        self.__s3 = side3
        
    def get_perimeter(self):
        if(self.__s1<self.__s2 + self.__s3 and self.__s2<self.__s3+self.__s1 and self.__s3 < self.__s2 + self.__s1):
            if(self.__s1==self.__s2 or self.__s2==self.__s3 or self.__s3==self.__s1):
                if(self.__s1==self.__s2==self.__s3):
                    print("\n---------------Perimeter of equilateral Triangle----------------- \n")
                    print(self.__s1 + self.__s2 + self.__s3)
                else:
                    print("\n---------------Perimeter of isoceles Triangle----------------- \n")
                    print(self.__s1 + self.__s2 + self.__s3)
            else:
                print("\n---------------Perimeter of scalene Triangle----------------- \n")
                print(self.__s1 + self.__s2 + self.__s3)      
        else:
            print(" \n Lengths of side are invaid. Hence, Triangle cannot be formed  \n ")
            
    def get_area(self):
        if(self.__s1<self.__s2 + self.__s3 and self.__s2<self.__s3+self.__s1 and self.__s3 < self.__s2 + self.__s1):
            s = (self.__s1 + self.__s2 + self.__s3 )/2
            if(self.__s1==self.__s2 or self.__s2==self.__s3 or self.__s3==self.__s1):
                if(self.__s1==self.__s2==self.__s3):
                    print("\n---------------Area of equilateral Triangle----------------- \n")
                    print(sqrt(s*(s-self.__s1)*(s-self.__s2)*(s-self.__s3)))
                else:
                    print("\n---------------Area of isoceles Triangle----------------- \n")
                    print(sqrt(s*(s-self.__s1)*(s-self.__s2)*(s-self.__s3)))
            else:
                print("\n---------------Area of scalene Triangle----------------- \n")
                print(sqrt(s*(s-self.__s1)*(s-self.__s2)*(s-self.__s3)))   
            # s = (self.__s1 + self.__s2 + self.__s3 )/2
            # print("\n--------------- Area of Trinagle----------------- \n")
            # print(sqrt(s*(s-self.__s1)*(s-self.__s2)*(s-self.__s3)))
        else:
             print("Cannot Form Triangle  \n ")

while True:
   side =  eval(input("\n\n enter 3 : For triangle \n enter 4 : for rectangle \n enter 5 : to exit  \n \n "))
   if side == 4:
       a = eval(input("enter side1 :"))
       b = eval(input("enter side2 :"))
       rect  = Rectangle(a,b)
       rect.get_perimeter()
       rect.get_area()
       
   elif side == 3:
       a = eval(input("enter side1 :"))
       b = eval(input("enter side2 :"))
       c = eval(input("enter side 3 :"))
       tri = Triangle(a,b,c)
       tri.get_perimeter()
       tri.get_area()
    
   elif side == 5:
        print(" OOPS you have exited")
        break