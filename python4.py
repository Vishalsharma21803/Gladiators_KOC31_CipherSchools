class Bird:
    def intro(self):
        print("This is bird class")

    def flight(self):
        print("Birds fly")

class Parrot(Bird):
    def flight(self):
        print("Parrot can fly")


class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")
obj1= Bird()
obj2= Parrot()
obj3= Ostrich()

obj1.flight()
obj2.flight()
obj3.flight()