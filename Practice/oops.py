class Student:
    #the below block defines attributes
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def describe(self):
        print("the name of boy is", self.name,"and his age is", self.age )

s1 = Student('Sabal Niroula', 19)
s1.describe()