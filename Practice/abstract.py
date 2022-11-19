from abc import *
import math 

class Myclass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass

class Sub1(Myclass):
    def calculate(self, x):
        print("Square of {} is {}".format(x, x*x))


class Sub2(Myclass):
    def calculate(self, x):
        print("Square root of {} is {}".format(x, math.sqrt(x)))


class Sub3(Myclass):
    def calculate(self, x):
        print("Cube of {} is {}".format(x, x**3))


obj1 = Sub1()
obj1.calculate(2)

obj2 = Sub2()
obj2.calculate(4)

obj1 = Sub3()
obj1.calculate(5)
