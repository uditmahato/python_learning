class Employee:
    def __init__(self,fn,ln) :
        self.fn=fn
        self.ln=ln
    def calculateSalary(self):
        print('I am  base class')

class FullTime(Employee):
    def calculateSalary(self):
        print('I am  Full Time Employee')

class PartTime(Employee):
    def calculateSalary(self):
        print('I am part time Employee')

f=FullTime('umesh','regmi')
f.calculateSalary()

g=PartTime('umesh','regmi')
g.calculateSalary()