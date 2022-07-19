
import time as t
from datetime import *

class Time:
    def __init__(self):
            print("In Answer just enter option character")
            self.__result = 0
            self.__startTime = 0 
            self.__endTime = 0
    def test(self):
      start = input("Press enter  start to begin the test  : ")
      if(start ==  "start"):
            self.__startTime = t.time()
            self.__startDetail = datetime.now().strftime("%H:%M:%S")
            input("Enter Your Name  : ")
            print("Which feature of OOP indicates code reusability?")
            print("a.Inheritance \nb.Polymorphism \nc.Encapsulation \nd.Abstraction")
            ans = input("Ans:")
            if(ans == "a" or ans == "A"):
              self.__result += 1
            elif ans != "b" or ans !="B" or ans != "c" or ans !="C" or ans != "d" or ans !="D":
              raise Exception("Invalid Input")
            
            print("Which of the following is Object Oriented language?")
            print("a.C \nb.C++ \nc.Prolog \nd.Lisp")
            ans = input("Ans:")
            if(ans == "b" or ans == "B"):
              self.__result += 1
            elif ans != "a" or ans !="A" or ans != "c" or ans !="C" or ans != "d" or ans !="D":
              raise Exception("Invalid Input")

            print("Which of the following is finite contiguous storage of data elements?")
            print("a.Array \nb.Linked List \nc.Tree \nd.Heap")
            ans = input("Ans:")
            if(ans == "a" or ans == "A"):
              self.__result += 1
            elif ans != "b" or ans !="B" or ans != "c" or ans !="C" or ans != "d" or ans !="D":
              raise Exception("Invalid Input")
            self.__endTime = t.time()
            self.__endDetail = datetime.now().strftime("%H:%M:%S")
            print(f'Result => {self.__result}\nStart Time => {self.__startDetail}\nEnd Time => {self.__endDetail}\nTime Taken => {self.__endTime - self.__startTime} seconds')
            
      else:
        raise Exception("Invalid input to begin test")



time = Time()
time.test()





# 5. Which feature of OOP indicates code reusability?
# a) Abstraction
# b) Polymorphism
# c) Encapsulation
# d) Inheritance
