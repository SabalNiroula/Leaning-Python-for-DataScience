class Teacher:
    def __init__(self):
        self.name1 = "harihar pandey"

    def display(self):
        print("the name is", self.name1)

class Student(Teacher):
    def __init__(self):
        super().__init__()
        super().display()

        self.name = "shyamlal pandit"

    def display(self):
        print("the name is", self.name)

s = Student()
s.display()