class Teacher:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name 

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address
    
    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary


class Student(Teacher):

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


s = Student()
s.setName("Sabal Niroula")
s.setId("2020116334")
s.setMarks(300)
s.setAddress("SundarHaraicha -7")

print(s.getName(), s.getAddress(), s.getId(), s.getMarks())