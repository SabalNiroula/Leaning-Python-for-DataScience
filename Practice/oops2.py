class Student:

    def setValues(self, name, marks):
        self.name = name
        self.marks = marks

    def getName(self):
        return (self.name)
        
    def getMarks(self):
        return (self.marks)

name = input("Enter your name ")
marks = int(input("Enter your marks: "))

s1 = Student()
s1.setValues(name, marks)
print(s1.getName)
print(s1.getMarks)