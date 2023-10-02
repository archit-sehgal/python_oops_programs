class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name of person is {self.name}\nAge of persson is {self.age}")

class Student(person):
    def __init__(self,section):
         self.section=section
         super().__init__("Archit","20")
    def displayStudent(self):
        print(f"Name of person is {self.name}\nAge of person is {self.age}\nSection of student is {self.section}")
call=Student("a")
call.displayStudent()