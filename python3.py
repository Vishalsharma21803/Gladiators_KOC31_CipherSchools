#inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)

class Employees(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age) #inheriting from person

a = Employees("Anurag", "55")
a.display()
