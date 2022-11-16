class Student:

    def setValues(self, name, marks):
        self.name = name
        self.marks = marks

    def getName(self):
        return (self.name)
        
    def getMarks(self):
        return (self.marks)
    
    class Detail:

        def __init__(self, address):
            self.address = address
        
        def display(self):
            print("address:",self.address)

name = input("Enter your name ")
marks = int(input("Enter your marks: "))

s1 = Student()
s1.setValues(name, marks)
print(s1.getName())
print(s1.getMarks())

dtl = Student.Detail("haraicha")
dtl.display()