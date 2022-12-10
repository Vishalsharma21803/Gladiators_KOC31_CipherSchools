#inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)

class Employees(Person):
    pass

a = Employees("Anurag", "35")
a.display()
