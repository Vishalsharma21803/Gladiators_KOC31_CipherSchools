class Student:
    def _init_(self, name, reg):
        self.name = name
        self.reg = reg
        
    def pr(self):
        print("Hello my name is "+self.name)
        
obj = Student("Ambashish Kumar Sharma","511553")
obj.pr()
